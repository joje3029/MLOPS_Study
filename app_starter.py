from flask import Flask
from flask_restx import Api, Resource, reqparse
import os
from datetime import datetime
from datetime import datetime
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import json
import requests

from data_from_yf import data_from
from lstm import lstm
from test.maria_test import get_from_db
from data_from_yf_api import data_from_yf_api
from insert_result import insert_result
from select_result import select_result

if __name__ == '__main__':
    app = Flask(__name__)
                #version : API 버전을 나타냄.       #API문서의 간단한 설명         #Swagger UI의 엔드포인트 URL을 지정함. 이 URL을 통해 Swagger UI에 접근할 수 있음.
    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
                                # title : Swagger UI에서 표시되는 API 문서의 제목
    test_api = api.namespace('test', description='조회 API') # api에 이름을 붙임. api 구분하려고
    #api 즉 야후파이낸스에 직접 접근.
    data = api.namespace('Develop', description='데이터 get API')
    #Db 전용
    data_from_db = api.namespace('datafromdb', description='Getting data from DB')

    #1번 API
    # 조회 API의 경로 -> 그래서 포트 9999로 해서 브라우저에 로컬 치면 hello world가 나옴
    @test_api.route('/')
    class Test(Resource): #Resource = flask restx의 Resource를 상속받아서 만들어짐. get.post등 에 대한 동작 정의
        def get(self): 
            return 'Hello World!'
    #이 코드는 / 경로에 대한 Get요청이 발생하면 Hello World!라는 문자열을 반환하는 엔드포인트 생성.

    parser = reqparse.RequestParser()
    parser.add_argument('start', type=str, help='Start date for data retrieval')
    parser.add_argument('end', type=str, help='End date for data retrieval')
        
    #2번 API
    # 데이터 get API의 경로 ->데이터를 가져옴. 
    @data.route('/get-data') #기존대로 / 로 하면 getData부분과 아래의 GetFromDB 부분의 엔드포인트가 충돌해서 
    class GetData(Resource):
        def get(self):
            #얘는 json으로 주니까.
            args = parser.parse_args() # 들어온걸 파싱해서
            result = data_from(args) #data_from에 넘김 그 결과를 result로 받고 
            return lstm(result) #result를 인자로 lstm.py에 줌. 그리고 lstm.py가 일한걸 넘김.

    #3번 API
    @data.route('/get-from-db')
    class GetFromDB(Resource):
        def get(self):
            args = parser.parse_args()
            s = datetime.strptime(args['start'], '%Y-%m-%d')
            e = datetime.strptime(args['end'], '%Y-%m-%d')

            print(s,e,type(s))
            
            result = get_from_db(s,e)
            
            return lstm(result)
    #4번 API  
    @data.route('/get-data-todb')
    class GetDataToDB(Resource):
        def get(self):
            # 야후파이낸스에 가서 주식 결과 가져옴. 
            result = data_from_yf_api()

            # 근데 학습 시키기 전에 db에 오늘꺼를 db에 insert 시킴.
            insert_result(result) #이건 insert만 하면 끝나.
            #이걸또 다 가꼬와서 학습
            query_result= select_result() # json 형태로 가져옴
            print(query_result)
            lstm_result=lstm(query_result) # 내부에서 json을 pandas로 바꿔서 함.
            
            return lstm_result

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)
