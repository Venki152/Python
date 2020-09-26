# Write a function called FindLarger that accepts two integer arguments arg1 and arg2.

#•In the function, print the larger number on the screen
#Sample  Output:

#Inside the Function, the Larger Number is: arg1      # assuming arg1 is larger
#•Where the function was called from, print the smaller number on the screen there
#Sample  Output:

#Outside the Function, the Smaller Number is: arg2        #assuming arg2 is smaller

#Run the function for the following values of arg1 and arg2
#•arg1 = 5, arg2 = 10
#•arg1 = 9, arg 2 = 18
#•arg1 = 5, arg 2 = 5


def FindLarger(arg1,arg2):  #function for checking larger values between two arguments
    if type(arg1) != int or type(arg2) != int:
        print('Check your input, Please enter numbers only') #if either values not number show warning
    elif (arg1 > arg2):
        print('Larger Number is ', arg1)  #print larger number
        return  arg2                      # return smaller number
    elif arg1 < arg2 :
        print('Larger Number is ', arg2)
        return arg1
    elif arg1 == arg2:
        return 'Warning!!! both arguments are equal'   #return warning is both values are equal
    


result = FindLarger(5, 10)
print ('Smaller Number is: ' , result, "\n")

result = FindLarger(9, 18)
print ('Smaller Number is: ' , result, "\n")

result = FindLarger(5, 5)
print ('Smaller Number is: ' , result, "\n")


arg1 = int(input('Input number for arg1: '))
arg2 = int(input('Input number for arg2: '))
FindLarger(arg1,arg2)
