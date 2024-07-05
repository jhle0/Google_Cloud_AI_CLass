from flask import Flask, render_template, request, make_response
from flask_restx import Api, Resource, fields


app = Flask('__name__')

api = Api(app, version='1.0', title='Sil2 register API',
          description='실습문제2 API with Swagger (flask-restx)')    # Swagger API

ns = api.namespace('users', description='User Operations')


user_model = api.model('User', {
    'userid': fields.String(required=True, description='User id'),
    'pwd1': fields.String(required=True, description='User pwd1'),
    'pwd2': fields.String(required=True, description='User pwd2'),
    'level': fields.String(required=True, description='User level'),
    'fullname': fields.String(required=True, description='User fullname'),
    'email': fields.String(required=True, description='User email'),
    'tel': fields.String(required=True, description='User tel'),
    'skill': fields.String(required=True, description='User skill'),
})


USER_DB = []


@ns.route('/')
class UserList(Resource):
    @ns.doc('user_lists')
    @ns.marshal_list_with(user_model)
    def get(self):
        """리스트 모든 사용자"""
        return USER_DB

    @ns.doc('user_create')
    @ns.expect(user_model, validate=True)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """새로운 사용자 생성"""
        user = api.payload
        USER_DB.append(user)
        return user, 201

api.add_namespace(ns)


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
