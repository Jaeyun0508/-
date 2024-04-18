def rep_char(c,n):
    print(c*n)

def draw_line_string(prompt):
    length=len(prompt)
    rep_char("_",2*length)
    
name=input("input his/her name: ")
text1="Hello "+name
text2="Welcome to Seoul"
draw_line_string(text1)
print(" ")
print(text1)
print(text2)
draw_line_string(text1)
