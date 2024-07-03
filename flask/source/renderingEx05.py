# 탬플릿 상속

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('super_init.html',
                           my_string='템플릿 상속 테스트',
                           my_lists=[11, 22, 33, 44, 55, 66, 77])


if __name__ == '__main__':
    app.run()




