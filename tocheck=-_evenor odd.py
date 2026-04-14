n=int(input('Enter the number:'))
if n>-1 and n%2==0:
    print('The number is positive and even')
elif n<0 and n%2==0:
    print('The number is negative and even')
elif n>0 and n%2!=0:
    print('The number is positive and odd')
elif n<0 and n%2!=0:
    print('The number is negative and odd')
else:
    print('Invalid')
