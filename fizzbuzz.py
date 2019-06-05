n = int(input(" Insert the number: "))
for i in range(n):
    if n%3 ==0:
        print("fizz")
    elif n%5==0:
        print("buzz")
    elif n%15==0:
        print("fizzbuzz")
    else:
        print(i)



