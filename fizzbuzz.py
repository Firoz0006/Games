
def FizzBuzz(r):
    r=input("Enter the number upto play")
    i=int(r)
    for i in range(1,i+1):
        if(i%3==0 and i%5==0):
            print(i,"FizzBuzz")
        else:
            if(i%3==0):
                print(i,"Fizz")
            else:
                if(i%5==0):
                    print(i,"Buzz")
                else:
                    print(i)
FizzBuzz(100)