from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user database
USER_DB = [
    {'id': 1, 'name': 'gildong', 'email': 'gildong@hwalbin.dang'},
    {'id': 2, 'name': 'gwansun', 'email': 'gwansun@manse.com'}
]


# 모든 사용자 정보 조회
@app.route('/')
def index():
    return render_template('index.html', users=USER_DB)



# 사용자 추가
@app.route('/add', methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        new_id = max(user['id'] for user in USER_DB) + 1
        new_user = {
            'id': new_id,
            'name': request.form['userName'],
            'email': request.form['userEmail']
        }
        USER_DB.append(new_user)
        return redirect(url_for('index'))
    return render_template('add_user.html')




# 사용자 수정
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = next((user for user in USER_DB if user['id'] == user_id), None)
    if request.method == 'POST':
        user['name'] = request.form['userName']
        user['email'] = request.form['userEmail']
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)




# 사용자 삭제
@app.route('/delete/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    global USER_DB
    USER_DB = [user for user in USER_DB if user['id'] != user_id]
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
