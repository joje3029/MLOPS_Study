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

if __name__ == '__main__':
    app = Flask(__name__)
                #version : API 버전을 나타냄.       #API문서의 간단한 설명         #Swagger UI의 엔드포인트 URL을 지정함. 이 URL을 통해 Swagger UI에 접근할 수 있음.
    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")
                                # title : Swagger UI에서 표시되는 API 문서의 제목
    test_api = api.namespace('test', description='조회 API') # api에 이름을 붙임. api 구분하려고
    data = api.namespace('Deveelope', description='데이터 get API')

    #Db 전용
    data_from_db = api.namespace('datafromdb', description='Getting data from DB')


    # 조회 API의 경로 -> 그래서 포트 9999로 해서 브라우저에 로컬 치면 hello world가 나옴
    @test_api.route('/')
    class Test(Resource): #Resource = flask restx의 Resource를 상속받아서 만들어짐. get.post등 에 대한 동작 정의
        def get(self): 
            return 'Hello World!'
    #이 코드는 / 경로에 대한 Get요청이 발생하면 Hello World!라는 문자열을 반환하는 엔드포인트 생성.

    parser = reqparse.RequestParser()
    parser.add_argument('start', type=str, help='Start date for data retrieval')
    parser.add_argument('end', type=str, help='End date for data retrieval')
        
    # 데이터 get API의 경로 ->데이터를 가져옴. 
    @data.route('/')
    class GetData(Resource):
        def get(self):
            #얘는 json으로 주니까.
            result = data_from(self) #data_from_yf에서 return한 json값을 lstm.py에게 리턴

            return lstm(result)

    @data.route('/')
    class GetFromDB:
        def get(self):
            s = requests.args.get('s',1,str)
            e = requests.args.get('e',1,str)
            print(s,e,type(s))
            return maria_test.get_from_db(s,e)
            
  
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)
