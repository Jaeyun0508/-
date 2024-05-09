shopping_bag=[]
num={}
while True:
    item=input('상품명? ')
    if (item==''):
        break
    n=int(input('수량은? '))
    num[item]=n
    shopping_bag.append(item)
    print(f'장바구니에 {item} {num[item]}개가 담겼습니다.')
    print()


n=len(shopping_bag)
print('\n>>>장바구니 보기: {',end='')
for i in range(0,n,1):
    print(f'{shopping_bag[i]}: ',end='')
    fruit=shopping_bag[i]
    print(num[fruit],end='')
    if i!=(n-1) :
        print(', ',end='')
print('}')

print('\n[검색]')
search=input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{search}은(는) {num[search]}개 담겨 있습니다.')
