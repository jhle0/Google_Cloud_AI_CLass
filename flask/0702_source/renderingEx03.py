print()
'''
    Jinja2 템플릿 표현식    

  {%                 # block_start_string
        hello = []
  %}                 # block_end_string
  
  {{                 # variable_start_string 
  
  }}                 # variable_end_string 

  {#                 # comment_start_string
  
  #}                 # comment_end_string
'''
from jinja2 import Template

template1 = Template('Hello {{ something }}')
print(template1.render(something='YuGwanSun'))

template2 = Template('{% for i in range(1, 10) %} {{ i }} {% endfor %} ')
print(template2.render())








