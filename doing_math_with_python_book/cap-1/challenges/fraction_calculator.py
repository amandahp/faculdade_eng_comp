from fractions import Fraction

'''
  Fraction Calculator
'''


def add(a, b):
  print(f'Result of Addition: {a+b} ')


def subtract(a, b):
  print(f'Result of Subtraction: {a-b}')

def multiply(a, b):
  print(f'Result of Multiply: {a*b}')

def divide(a, b):
  print(f'Result of Divide: {a/b}')

if __name__ == '__main__':
  a = Fraction(input('Enter first fraction: '))
  b = Fraction(input('Enter second fraction: '))
  
  option = input('Operation to perform - Add, Subtract, Divide, Multiply: ')
  
  if option == 'Add':
    add(a, b)
  elif option == 'Subtract':
    subtract(a, b)
  elif option == 'Divide':
    divide(a, b)
  elif option == 'Multiply':
    multiply(a, b)
  else:
    print('Invalid Operation')