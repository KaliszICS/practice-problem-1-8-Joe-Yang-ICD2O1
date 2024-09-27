
def q1():
  #Write Assignment code here
  num1= True
  num2= False
  print(num1 and num2)
  print(num1 or num2)


def q2():
  #Write Assignment code here
  num1= input("Enter an integer: ")
  print(num1 not 0)


def q3():
  #Write Assignment code here
  num1= input("Enter a number: ")
  print(num1 > 0 and num1 < 10)

def q4():
  #Write Assignment code here
  num1= input("Input a food: ")
  num2= input("Input a drink: ")
  print(not num1=='pizza' and not num2== 'pop')


def q5():
  #Write Assignment code here
  num1 = input("Enter an integer: ")
  print(f"The integer {num1} is {num1 % 2 == 0}")

#Do not edit code after this
#Comment out the followwing code when running tests
'''
q1()
q2()
q3()
q4()
q5()
'''