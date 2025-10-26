p=input("Enter your new password:  ")
l=0
if len(p) >=10:
    l=1
else:
    print("length of password should be greater than or equal to 10")
u=0
if any(c.isupper() for c in p):
    u=1
else:
    print("any of the character should be in upper case")
t=0
if any(c.islower() for c in p):
    t=1
else:
    print("any of the character should be in lower case")
d=0
if any(c.isdigit() for c in p):
    d=1
else:
    print("there should be any one digit")
c=0
if any(c in "@,#,$,&,!,?,%,^" for c in p):
    c=1
else:
    print("there should be any of the special characters")
if all([l==1, u==1, t==1, d==1, c==1]):
    print("Your password is strong")
else:
    print("Your current password is weak")