import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
import getdata_from_db

# watchdog는 파일을이 떨궈지나(이벤트가 무리없이 이뤄지나)만 봄. => 예외처리고 나발이고 다해야함.

class Target: #와치도그가 볼 타겟
    watchDir = os.getcwd()
    watchDir = 'MLops\collect_files' # 여기의 collect_files는 data_from_yf_api를 실행한 결과를 저장 -> 즉 이거를 멍뭉이가 지켜보고 있다가 안하면 멍!
    #watchDir에 감시하려는 디렉토리를 명시한다.

    def __init__(self):
        self.observer = Observer()   #observer객체를 만듦 : observer- 소프트웨어 디지아니 패턴 중 하나. 주로 객체 간의 상태 변화를 감지하고 통지하는데 사용. 주로 이벤트 핸들링 시스템이나 구독 및 게시 시스템에서 적용됨.

    def run(self): # 구동했다.
        print('Watcher is Started.')
        event_handler = Handler() # 이벤트 핸들러함수
        self.observer.schedule(event_handler, self.watchDir, 
                                                       recursive=True) #스케쥴러 세팅 : 이벤트핸들러 세팅, 스
        self.observer.start() # 
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()

class Handler(FileSystemEventHandler):
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함
    #파일, 디렉터리가 move 되거나 rename 되면 실행
    '''
    def on_moved(self, event):
        print(event)
    '''
    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        print(event)
        getdata_from_db.insert_data()
        print("Insert func completed")
    '''
    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)
    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)
    '''
if __name__ == "__main__": #본 파일에서 실행될 때만 실행되도록 함
    w = Target()
    w.run()