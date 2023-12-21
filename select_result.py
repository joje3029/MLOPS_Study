import pymysql # 설치하고 인터프리터를 설정
import pandas as pd
from sqlalchemy import create_engine

# con = pymysql.connect(host='localhost', user='root', password = '', db='samsung', charset='utf-8')
con = pymysql.connect(host='localhost', user='root', password='', db='samsung', charset='utf8mb4')


query = 'select * from samsung.20231219'
df = pd.read_sql_query(query, con)
reult=df.to_json()
print(reult)
print(len(df))

def select_result():
    con = pymysql.connect(host='localhost', user='root', password='', db='samsung', charset='utf8mb4')

    query = 'select * from samsung.20231219'
    df = pd.read_sql_query(query, con)
    return df



# pymysql.install_as_MySQLdb
# engine = create_engine("mysql://user:password@host/db")
# df.to_sql(name='new_performance_log', con=engine, if_exists='append', index=False) # append : table
