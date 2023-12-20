from datetime import datetime
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import json



yf.pdr_override() # pandas_datareaderdml get_data_yahoo 함수를 yfinance 모듈로 덮어쓰기(override)함.
#기본적으로 pandas_datareader는 Yahoo Finance API를 통해 주가 데이터를 가져오는데, 이 API는 변경사항이나 서비스 중단과 같은 이슈로 인해 정상적으로 작동하지 않을 때가 많지만 이친구는 직접 액세스해서 데이터를 가져옴.

def data_from(args):            
    start_date = datetime.strptime(args['start'], '%Y-%m-%d')
    end_date = datetime.strptime(args['end'], '%Y-%m-%d')
    filename = datetime.now().strftime("%Y%m%d_%H%m%S")

    yf.pdr_override() # 아후파이낸스 위에 적혀있음.
    #삼성 주식코드
    # df = pdr.get_data_yahoo('005930.KS', start_date, end_date)
    
    #s&p500 주식코드
    df = pdr.get_data_yahoo('^GSPC', start_date, end_date)
        
    #판다스를 json으로 변환
    json_data = df.to_json(orient='records')
    
    #변환한 json 값을 retrun 
    return json_data # 이 값을 lstm.py에 넘겨야하는거잖아.

