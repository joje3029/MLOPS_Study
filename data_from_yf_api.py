from datetime import datetime, timedelta
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import json



yf.pdr_override() # pandas_datareaderdml get_data_yahoo 함수를 yfinance 모듈로 덮어쓰기(override)함.
#기본적으로 pandas_datareader는 Yahoo Finance API를 통해 주가 데이터를 가져오는데, 이 API는 변경사항이나 서비스 중단과 같은 이슈로 인해 정상적으로 작동하지 않을 때가 많지만 이친구는 직접 액세스해서 데이터를 가져옴.

# 현재 날짜와 시간을 얻기
# now = datetime.now()
# print(type(now)) #datetime
# print(now)

# 현재 날짜 및 시간을 문자열로 표현
now_str = '2023-12-22 18:31:06.774978'

# 문자열을 datetime 객체로 변환
now = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S.%f')

# 어제 날짜 계산
yesterday = now - timedelta(days=1)

# 현 날짜의 전날 날짜와 시간 구하기
yesterday = now - timedelta(days=1)
start_date = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
end_date = yesterday.replace(hour=23, minute=59, second=59, microsecond=0)

# s&p500 주식코드
df = pdr.get_data_yahoo('^GSPC', start_date, end_date)
json_data = df.to_json(orient='records')

# 전날 날짜 json
yesterday_str = yesterday.strftime("%Y-%m-%d")
yesterday_date = {"Date": yesterday_str}

# 리스트에 새로운 json 객체 추가
json_data_list = [yesterday_date]

# 기존의 json 데이터를 리스트에 추가
json_data_list.extend(pd.read_json(json_data, orient='records').to_dict('records'))

print(json_data_list) #[{'Date': '2023-12-21'}, {'Open': 4724.2900390625, 'High': 4748.7099609375, 'Low': 4708.3500976562, 'Close': 4746.75, 'Adj Close': 4746.75, 'Volume': 3431180000}]




def data_from_yf_api():
    # 현재 날짜와 시간을 얻기
    #now = datetime.now() #어제가 빨간날이여서 주식 결과가 없으셔. 일단 있는 날짜로 때림
    now_str = '2023-12-22 18:31:06.774978'

    # 문자열을 datetime 객체로 변환
    now = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S.%f')

    # 어제 날짜 계산
    yesterday = now - timedelta(days=1)

    # 현 날짜의 전날 날짜와 시간 구하기
    yesterday = now - timedelta(days=1)
    start_date = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = yesterday.replace(hour=23, minute=59, second=59, microsecond=0)

    # s&p500 주식코드
    df = pdr.get_data_yahoo('^GSPC', start_date, end_date)
    json_data = df.to_json(orient='records')

    # 전날 날짜 json
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    yesterday_date = {"Date": yesterday_str}

    # 리스트에 새로운 json 객체 추가
    json_data_list = [yesterday_date]

    # 기존의 json 데이터를 리스트에 추가
    json_data_list.extend(pd.read_json(json_data, orient='records').to_dict('records'))
    
    # 파일명을 result_yesterday.txt로 동적으로 생성
    result_filename = f'result_{yesterday_str}.txt'

    # 파일명을 result_yesterday.txt로 동적으로 생성
    result_filename = f'C:\\Users\\admin\\sominAI\\MLops\\collect_files\\result_{yesterday_str}.txt'

    # 변환한 json 값을 result_yesterday.txt 파일로 저장
    pd.DataFrame(json_data_list).to_csv(result_filename, index=False, sep='\t')

    #변환한 json 값을 retrun 
    return json_data_list # [{"Open":4764.7299804688,"High":4778.009765625,"Low":4697.8198242188,"Close":4698.3500976562,"Adj Close":4698.3500976562,"Volume":4201320000}]
    # 당일꺼가 나올꺼야.
