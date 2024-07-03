# Jinja2 template 주요 문법, 함수

from jinja2 import Environment, FileSystemLoader

# file이 들어있는 디렉토리 지정
file_loader = FileSystemLoader('./templates')


# 환경 호출
env = Environment(loader=file_loader)


# 텍스트 파일로도 렌더링 가능
template = env.get_template('helloWorld.txt')
print(template.render())
print('-'*40)


# jinja2 변수 지정하는 문법도 그대로 텍스트 파일을 이용하여 렌더링 가능
template2 = env.get_template('dogs.txt')
print(template2.render(name='simdang', species='풍산개'))
print('-'*40)


# 객체에 대한 접근도 가능하다
template3 = env.get_template('personInfo.txt')
person = {}
person['name'] = '율곡이이'
person['salary'] = 10000

print(template3.render(data=person))
print('-'*40)


# 논리값도 렌더링 가능
template4 = env.get_template('ifStructure.txt')
print(template4.render(boolean=False))
print('-'*40)


# 리스트도 가능
template5 = env.get_template('forColor.txt')
colors = list('빨주노초파남보')
print(template5.render(rainbow=colors))
print('-'*40)







