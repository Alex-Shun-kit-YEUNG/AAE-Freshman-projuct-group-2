def function1():
    print('This text represent the content of function 1')  
    print('Ellen') 
    print('Alex') 
    print('Ryan') 
    print('joe')
    

def function2():
    print('This text represent the content of function 2')  
    a = 5
    b = 7
    c = 9
    sum = a+b+c
    print('a =',a,'b =',b,'c =',c,'sum =',sum)
    

def function3():
    print('This text represent the content of function 3')  
    a = 5
    print('a =',a,',','Square of a:',a**2)

def function4():
    print('This text represent the content of function 4')  
    a = 5
    b = 4
    print('a =',a,'b =',b)
    if a>b:
        print('a is larger than b')
    elif a<b:
        print('a is smaller than b')
    elif a == b:
        print('a is equal to b')

#The Main function edited by Group leader
print('This is ENG1003'' Week 3 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')   #Ask for an integer

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
else:
    print('There is no function', inp)

