from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>Hello Flask World</h1>'

@app.route("/user/<username>")
def get_user(username):
    return 'user : '+username

if __name__ == '__main__':
    #test_request_context() : Flask 객체 내장 메소드, HTTP 요청을 테스트할 수 있는 메소드
    with app.test_request_context():
        print(url_for('hello'))
        print(url_for('get_user', username='gildong'))
