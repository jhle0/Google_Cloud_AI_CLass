# Flask 에서 HTTP 요청과 응답을 처리하기 위해서는
# Request, Response 객체를 사용
# flask 모듈에서 호출

from flask import Flask, request

app = Flask(__name__)

# GET 방식으로 데이터를 서버로 가져오기
# http://127.0.0.1:5000/data?name=gildong
@app.route("/data")
def getRequest():
    return f"request 객체를 이용해서 주소창으로 넘어온 번수 name의 값은 {request.args.get('name')} 이다."


# HTTP 메시지는 웹서버와 웹스라우저간의 데이터 정송방식이 문자열 타입이 default

# http://127.0.0.1:5000/intData?num1=100
# 변수와 데이터 타입 모두 지정 가능
@app.route('/intData')
def getRequest2():
    numValue = request.args.get('num1', "0", int)    # args.get(변수명, default, datatype)

    result = numValue + 200
    return str(result)





if __name__=='__main__':
    app.run()










