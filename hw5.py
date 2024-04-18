def read_single_digit(num):
    if num==0:
        return "영"
    elif num==1:
        return "일"
    elif num==2:
        return "이"
    elif num==3:
        return "삼"
    elif num==4:
        return "사"
    elif num==5:
        return "오"
    elif num==6:
        return "육"
    elif num==7:
        return "칠"
    elif num==8:
        return "팔"
    else :
        return "구"

def read_number(num):
    n1=num//100
    n2=(num%100)//10
    n3=(num%100)%10
    nk1=read_single_digit(n1)
    nk2=read_single_digit(n2)
    nk3=read_single_digit(n3)
    numkor=f'{nk1} {nk2} {nk3}'
    return numkor

num=int(input("세 자리 정수 입력: "))
result=read_number(num)
print(result)
