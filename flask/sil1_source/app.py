from flask import Flask, render_template

app = Flask(__name__)

# 사용자 DB (model)
USER_DB = [
    {'id': 1, 'name': 'gildong', 'email': 'gildong@hwalbin.dang'},
    {'id': 2, 'name': 'gwansun', 'email': 'gwansun@manse.com'}
]


# index 페이지 - 전체 사용자 목록 조회
@app.route('/')
def index():
    return render_template('index.html', users=USER_DB)



if __name__ == '__main__':
    app.run(debug=True)













