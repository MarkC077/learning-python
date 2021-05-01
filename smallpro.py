print("Whats your couples name?")

name1 = input("What is your name? ")
name2 = input("What your partner name? ")


def couplesname(str1, str2):
    return name1[ : : 2] + name2[ : : 2]
    
result = couplesname(name1, name2)


print(f"Your couples names is {result}")

# we dont know why this code is here, but if you remove it, everything breaks, so here it will stay

reverse = input("Do you want to reverse the outcome? [y / n] ")


def reversename(str2, str1):

    if reverse == "Y" or reverse == "y":
        return name2[ : : 2] + name1[ : : 2]
    elif reverse == "N" or reverse =="n":
        print("Thank you for playing")
    else:
        print("Sorry that is the wrong input!")

result2 = reversename(name2, name1)

print(f"Your reverse name is {result2}")