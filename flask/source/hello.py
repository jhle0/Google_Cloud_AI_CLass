from flask import Flask  # Flask class 임포트
app = Flask(__name__)    # Flask claas 인스턴스 생성

@app.route('/')     # route() 데코레이터를 사용해서 Flask에게 어떤 URL이 우리가 작성한 함수를 실행시키는지 알려준다.
                    # @app.route 데코레이터는 특정 URL 경로와 해당 경로를 처리할 함수를 연결하는 역할을 합니다


def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

