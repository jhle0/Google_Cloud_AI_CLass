from flask import Flask, request
from datetime import  datetime

app = Flask(__name__)

# request.args : GET 방식만
# request.values : HTTP 메소드 타입에 상관없이 데이터를 처리할 수 있는 속석



# http://127.0.0.1:5000/data?name=gildong
@app.route("/data", methods=['GET', 'POST'])
def getRequest():
    return f"request 객체를 이용해서 주소창으로 넘어온 번수 name의 값은 {request.values.get('name')} 이다."



# HTTP 메시지는 웹서버와 웹스라우저간의 데이터 정송방식이 문자열 타입이 default

# http://127.0.0.1:5000/intData?num1=100
# 변수와 데이터 타입 모두 지정 가능
@app.route('/intData', methods=['GET', 'POST'])
def getRequest2():
    numValue = request.values.get('num1', "0", int)    # args.get(변수명, default, datatype)

    result = numValue + 200
    return str(result)

    # request 에 있는 args 는 GET 방식만 접근 가능하다





# type 값으로 파이썬에서 제공하는 기본 데이터 타입 외에도 개발자가 만든 함수, 클래스를 사용 가능
#       => 사용자 정의 데이터 타입으로 사용 가능

# 사용자 정의 함수 (특정한 날짜 형식을 지정하는 함수)
def userDateType(date_format):
    def changeFormat(date_string):
        # datetime.strptime(date_string, format)  : format에 맞는 date_string을 datetime 객체로 리턴하는 메소드
        return datetime.strptime(date_string, date_format)
    return changeFormat


# 사용자 정의 클래스
# __call__ 메소드를 정의해서 사용
class userDefineDateType:
    def __init__(self, format):
        self.format = format

    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)




# http://127.0.0.1:5000/date?date=2024-07-03
@app.route('/date', methods=['GET', 'POST'])
def getValue():
    time = request.values.get('date', default='2024-07-01', type=userDateType('%Y-%m-%d'))
    print(time)
    print(type(time))

    result = str(time)
    print(result)
    print(type(result))

    return result



import json

# http://127.0.0.1:5000/datetime?date=2024-07-03
@app.route('/datetime', methods=['GET', 'POST'])
def getValuse2():
    time = request.values.get('date', default='2024-07-01', type=userDefineDateType('%Y-%m-%d'))
    print(time)
    print(type(time))

    result = str(time)       # 웹브라우저에 return 되는 형식은 string
                             # 현재 result는 list이므로 올바른 형식(string)으로 브라우저로 나가지 못하는 상태
    print(result)
    print(type(result))

    return result



# http://127.0.0.1:5000/datelist?dates=2024-07-01&dates=2024-07-02
# 같은 변수에 여러 개의 값이 넘어오는 경우라면? 리스트 타입으로 받아서 반환해주면 된다
# 이 때 사용하는 함수 : getlist()


@app.route('/datelist', methods=['GET', 'POST'])
def getValueslist():
    times = request.values.getlist("dates", type=userDateType('%Y-%m-%d'))
    print(times)
    print(type(times))


    '''
    result = str(times)        # 웹브라우저에 return 되는 형식은 string
                              # 현재 result는 list이므로 올바른 형식(string)으로 브라우저로 나가지 못하는 상태
    print(result)
    print(type(result))
    '''

    result = []

    for time in times:
        result.append(str(time))

    print(result)

    return json.dumps(result)      # advanced




if __name__=='__main__':
    app.run(debug=True)

