from sqlalchemy import text # sql 질의어를 문자열 형태로 나타태고 처리하는데 사용. 
import sys # 파이썬 인터프리터와 관련된 기능을 제공함. 
sys.path.append('.') # 경로설정 #여기서는 sys의 path를 조작하여 현재 디렉토리를 모듈 검색 열로에 추가하는데 사용. 그니까 상대경로(웹 수업할때 다른데 있는거면 상대경로를 ../프로젝트명 이런식으로 해서 설정했잖아 그거야)
from project.common.maria_data_service import MariaDataService # project 패키지의 common 모듈 안에 있는 maria_data_service 모듈에서 mariaDataService 클래스를 가져옴. 
import app_starter # falsk 애플리케이션을 시작할때 사용할 app_starter.py import

maria_service = MariaDataService.instance() # 싱글톤 패턴으로 어떤 클래스가 최대 한번만 인스턴스화 되도록 하는 디자인 패턴 사용. 

def get_from_db(s,e): #s : 인자로 들어올 start 날짜, e : 인자로 들어올 end 날짜.
    sql = f"select * from samsung.20231219 where Date between '{s} and '{e}'"
    print(sql, type(sql)) #sql문 찍어보기
    test = maria_service.get(test(sql)) # 마리아 서비스에서 가져오고 sql 결과를 test 담음. 위의 sql 문의 날짜를 -> 즉 진짜 우리 samsung DB에서 가져옴.
    print(len(test), test[0], type(test)) # 결과 길이, 결과 테이블의 첫번째 행, 결과의 타입 확인
    return test #가져온 테이블을 retrun