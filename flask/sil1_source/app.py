from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)




# 문서화 작업 - API 만들기
from flask_restx import Api, Resource, fields

api = Api(app, version='1.0', title='Basic CRUD API',
          description='간단한 CRUD API with Swagger (flask-restx)')    # Swagger API

ns = api.namespace('users', description='User Operations')



# 사용자 DB (model)
USER_DB = [
    {'id': 1, 'name': 'gildong', 'email': 'gildong@hwalbin.dang'},
    {'id': 2, 'name': 'gwansun', 'email': 'gwansun@manse.com'}
]


# API 모델 정의
user_model = api.model('User', {
    'id': fields.Integer(readonly=True, descirption='User Identifier'),
    'name': fields.String(required=True, description='User name'),
    'email': fields.String(required=True, description='User email'),
})


# 모든 사용자 정보 조회
@app.route('/')
def index():
    return render_template('index.html', users=USER_DB)



# API
@ns.route('/')
class UserList(Resource):
    @ns.doc('user_lists')
    @ns.marshal_list_with(user_model)
    def get(self):
        return USER_DB

    @ns.doc('user_create')
    @ns.expect(user_model, validate=True)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        new_id = max(user['id'] for user in USER_DB) + 1
        new_user = api.payload
        new_user['id'] = new_id
        USER_DB.append(new_user)
        return new_user, 201










# 사용자 추가
@app.route('/add', methods=['GET', 'POST'])
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
    return render_template('add_user.html')     # GET 일 때




# 사용자 수정 - 사용자 정보 수정 from을 보여주고 수정 내용을 다시 DB에 등록
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = next((user for user in USER_DB if user['id'] == user_id), None)    # 사용자 확인
    if user is None:
        return "User not found", 404

    if request.method == 'POST':
        user['name'] = request.form['userName']
        user['email'] = request.form['userEmail']
        return redirect(url_for('index'))
    return render_template('edit_user.html', user=user)




# 사용자 삭제
@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    global USER_DB
    USER_DB = [user for user in USER_DB if user['id'] != user_id]
    return redirect(url_for('index'))


api.add_namespace(ns)



if __name__ == '__main__':
    app.run(debug=True)
