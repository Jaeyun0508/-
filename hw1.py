def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    area = radius*radius*3.14
    return area

input_prompt=input('넓이를 구하고자 하는 원의 반지름은?')
result=get_radius(input_prompt)
result2=get_circle_area(result)
print('반지름',result,'인 원의 넓이 = 3.14 x',result,'x',result,'=',result2)

