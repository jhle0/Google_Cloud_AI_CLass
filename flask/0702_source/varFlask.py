from flask import Flask

app = Flask(__name__)

@app.route('/user/<userName>')      # get방식으로 데이터 가져오기
def get_uri_name(userName):
    # biz logic 처리 코드 필요
    return 'user : ' + userName

if __name__ == '__main__':
    app.run()

#http://127.0.0.1:5000/user/gildong


