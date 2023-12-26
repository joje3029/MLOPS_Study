import pymysql # 설치하고 인터프리터를 설정
import pandas as pd
from sqlalchemy import create_engine

result_list=[{'Date': '2023-12-21'}, {'Open': 4724.2900390625, 'High': 4748.7099609375, 'Low': 4708.3500976562, 'Close': 4746.75, 'Adj Close': 4746.75, 'Volume': 3431180000}]

con = pymysql.connect(host='localhost', user='root', password='', db='samsung', charset='utf8mb4')

result_json0=result_list[0]
result_json1=result_list[1]

date=result_json0['Date']
open=result_json1['Open']
high=result_json1['High']
low=result_json1['Low']
close=result_json1['Close']
adj_close=result_json1['Adj Close']
volume=result_json1['Volume']


query = f"INSERT INTO samsung.20231219 (Date, Open, High, Low, Close, `Adj Close`, Volume) VALUES ('{date}', {open}, {high}, {low}, {close}, {adj_close}, {volume})"

# 쿼리 실행
try:
    with con.cursor() as cursor:
        cursor.execute(query)
    con.commit()
    print("Data inserted successfully.") # 테스트로 이것만 했을때 insert 잘됨. 확인함.
except Exception as e:
    print(f"Error: {e}")
finally:
    con.close()



def insert_result(result_list):
    # con = pymysql.connect(host='localhost', user='root', password = '', db='samsung', charset='utf-8')
    con = pymysql.connect(host='localhost', user='root', password='', db='samsung', charset='utf8mb4')
    
    print(result_list) 

    result_json0=result_list[0]
    print(result_json0)

    result_json1=result_list[1]
    print(result_json1)

    date=result_json0['Date']
    open=result_json1['Open']
    high=result_json1['High']
    low=result_json1['Low']
    close=result_json1['Close']
    adj_close=result_json1['Adj Close']
    volume=result_json1['Volume']


    query = f"INSERT INTO samsung.20231219 (Date, Open, High, Low, Close, `Adj Close`, Volume) VALUES ('{date}', {open}, {high}, {low}, {close}, {adj_close}, {volume})"

    # 쿼리 실행
    try:
        with con.cursor() as cursor:
            cursor.execute(query)
        con.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        con.close()


