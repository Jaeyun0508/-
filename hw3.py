discount_rate=0

def set_rate(rate):
    global discount_rate
    discount_rate=rate

def get_rate():
    return discount_rate

def get_fixed_price(price):
    fixed_price=price/(100-discount_rate)*100
    return fixed_price

def main():
    rate=int(input("할인율은?"))
    set_rate(rate)
    A_price=int(input("A 상품의 할인된 가격은?"))
    B_price=int(input("B 상품의 할인된 가격은?"))
    print("A 상품의 정가는 ",get_fixed_price(A_price),"원")
    print("B 상품의 정가는 ",get_fixed_price(B_price),"원")

if __name__=='__main__':
    main()
