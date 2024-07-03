from flask import Flask, Response, request

app = Flask(__name__)

# 쿠키 생성 / 확인 / 삭제

# http://127.0.0.1:5000/cookie_set
@app.route('/cookie_set')
def setCookie():
    res = Response('Cookie 객체 생성 중')
    res.set_cookie('cookieName', 'Hello Cookie')
    return res

# http://127.0.0.1:5000/cookie_status
@app.route('/cookie_status')
def statusCookie():
    return f"cookieName 쿠키는 {request.cookies.get('cookieName')} 값을 가지고 있다."


# http://127.0.0.1:5000/cookie_out
@app.route('/cookie_out')
def outCookie():
    res = Response("Cookie 삭제")
    res.set_cookie('cookieName', expires=0)     # 지속시간을 0으로 처리하여 삭제
    return res




if __name__ == '__main__':
    app.run()

