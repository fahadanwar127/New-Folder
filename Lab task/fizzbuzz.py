import random
def fizzbuzz(num):
    value = 0
    for i in range(1,num+1):
        i = random.randint(1,100)
        cv = value + i
        value = cv

        if i % 3 == 0 and i % 5 == 0:
            print ("fizzbuzz")
        elif i % 3 == 0:
            print ("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print (i)
fizzbuzz(15)