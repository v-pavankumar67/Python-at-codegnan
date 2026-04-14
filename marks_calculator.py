m=int(input('Enter the marks:'))
if 90<=m<=100:
    print('Grade is A')
elif 80<=m<=89:
    print('Grade is B')
elif 60<=m<=79:
    print('Grade is C')
elif 40<=m<=59:
    print('Grade is D')
elif  0<m<40:
    print('F')
else:
    print('Invalid marks')
