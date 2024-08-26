import random
def password_generator():

    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    symbols=['+','-','*','/','@','#','$','%','&','^']

    password=""

    x=int(input("enter number of letters:"))
    y=int(input("enter number of digits:"))
    z=int(input("enter number of symbols:"))
    print()

    for i in range(1,x+1):
        char=random.choice(letters)
        password+=char

    for i in range(1,y+1):
        char=random.choice(numbers)
        password+=char

    for i in range(1,z+1):
        char=random.choice(symbols)
        password+=char


    print("The random password is : " ,password)

password_generator()