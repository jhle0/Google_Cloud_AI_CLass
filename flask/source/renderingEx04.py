from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def render_test():
    # model 단 (biz logic)을 통해 응답될 데이터 생성
    str = "템플릿 테스트"
    result_list = [11, 22, 33, 44, 55]

    return render_template('template.html', my_string=str,
                           my_list=result_list)

if __name__ == '__main__':
    app.run(debug=True)