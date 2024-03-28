def exchange(money):
    a=money//500
    money=money%500
    b=money//100
    money=money%100
    c=money//50
    money=money%50
    d=money//10
    print("500원 동전의 개수: ",a)
    print("100원 동전의 개수: ",b)
    print("50원 동전의 개수: ",c)
    print("10원 동전의 개수: ",d)
    
def get_integer(prompt):
    money=int(input(prompt))
    return money

result=get_integer("동전으로 교환하고자 하는 금액은?")
exchange(result)
