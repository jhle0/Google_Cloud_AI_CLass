from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello Flask Index Page</h1>'

# String 타입의 userName 파라미터 (String 타입은 기본값)
@app.route("/user/<username>")
def show_user(username):
    return 'User name is %s' % username

# http://127.0.0.1:5000/user/gildong

# int 타입의 post-id 파라미터 지정
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f'Post ID : {post_id + 1}'

# http://127.0.0.1:5000/post/10

# float 타입의 r 파라미터 지정
@app.route('/circle/<float:r>')
def show_pi(r):
    return f'r : {r * 3.14}'

# http://127.0.0.1:5000/circle/5.0

if __name__ == '__main__':
    app.run()


























