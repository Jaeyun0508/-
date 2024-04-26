def display_multiplication_table(start,end):
    for i in range(1,10):
        for j in range(start,end+1):
            print(f'{j} x {i} = {j*i}', end='\t')
            if j==end:
                print()

display_multiplication_table(2,5)
print()
display_multiplication_table(6,9)
