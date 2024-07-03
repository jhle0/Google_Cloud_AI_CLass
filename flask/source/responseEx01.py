# flask에서 웹브라우저에 응답을 할 때 모든 데이터는 Response 객체를 이용한다.

# Response 객체를 생성할 때 사용하는 인자
# - response : 웹브라우저에게 응답할 데이터
# - status : HTTP 상태코드
# - header : 웹브라우저에게 응답할 header 정보
# - mimetype : image/jpeg, text/html 와 같이 HTTP 메시지 바디가 어떤 MINE TYPE 데이터인지 지정
# - content-type : mimetype과 같은 역할


# Response 객체에서 HTTP 메시지 바디를 설정하는 메소드
# - get_data : 브라우저에 응답할 데이터를 반환 (data 속성에 있는 값을 얻어올 때)
# - set_data : 브라우저에 응답할 데이터를 변경할 때
# - set_cookie : 사용자 쿠키를 설정




from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def res():
    res = Response('응답 객체 테스트')
    res.headers.add("webApp-Name", "Flask-Response")
    res.set_data("플라스크 응답 객체 확인")

    return res



if __name__ == '__main__':
    app.run()





