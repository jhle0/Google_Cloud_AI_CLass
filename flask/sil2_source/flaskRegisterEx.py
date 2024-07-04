from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask('__name__')

USER_DB = []


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = {
                'userid': request.form['userid'],
                'pwd1': request.form['pwd1'],
                'pwd2': request.form['pwd2'],
                'level': request.form['level'],
                'fullname': request.form['fullname'],
                'email': request.form['email'],
                'tel': request.form['tel'],
                'skill': request.form['skill'],
        }
        USER_DB.append(user)
        user_id = request.form['userid']
        print(f"사용자 ID: {user_id}")

        # 사용자 ID를 쿠키에 저장
        resp = make_response(render_template('register.html'))
        resp.set_cookie('userID', user_id)
        return resp

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
