from flask import Flask, render_template

# [주의] root 폴더 안에 templates 폴더를 만들고 그 곳에 template들 (HTML 파일) 을 두기!

app = Flask(__name__)

@app.route("/")
def main():
    return '<h1>Hello Jinja2 Template Engine</h2>'

@app.route("/user/<username>")
def user(username):
    return render_template('user.html', name=username)


if __name__ == '__main__':
    app.run()
