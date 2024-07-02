from flask import Flask

app = Flask(__name__)

# 라우팅 : 복잡한 URI를 쉽게 처리하도록 도와주는 기능
#       : route 데코레이터(@)를 사용

@app.route("/hello/")     # route를 통해서 주소(URI) 지정
def hello_flask():         # View 단 => view 함수
    return "Hello Flask World~!!!"

if __name__ == '__main__':
    app.run()


