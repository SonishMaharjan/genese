a= 1
b = 2
x=0
sum = 0

max=4000000


while a<=max:
    #print(a)

    if(a%2==0):
        sum+=a

    x=a+b
    a=b
    b=x


print("even sum= ",sum)
