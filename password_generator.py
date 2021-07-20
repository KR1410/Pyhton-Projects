import string
import random

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    #print(s1)
    s2 = string.ascii_lowercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)

    while(True):
        try:
            pw_length = int(input("enter length of password(should be greater than 6): "))
            if pw_length<=0:
                print("please enter a valid length")
            elif pw_length<7:
                print("password generated will be weak, enter a length greater than 6")
            else:
                break
        except Exception as e:
            print(e)
            print("please enter a valid length")
    pw = []
    pw.extend(list(s1))
    pw.extend(list(s2))
    pw.extend(list(s3))
    pw.extend(list(s4))

    random.shuffle(pw)

    print("".join(pw[0:pw_length])) #will join every element of list