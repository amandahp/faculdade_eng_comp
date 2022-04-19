from fractions import Fraction

def fraction_number():
  try:
    a = Fraction(input("Enter a fraction: "))
    print(a)
  except ZeroDivisionError:
    print("Invalid fraction")


def complex_number():
  z = complex(input("Enter a complex number: "))
  print(z)


def is_factor(a, b):
  if b % a == 0: 
    return True
  else:
    return False


def range_fun():
  for i in range(1, 4):
    print(i)
  for j in range(5):
    print(j)
  for k in range(1, 10, 2):
    print(k)

range_fun()


'''
  Find the factors of an integer
'''

def factors(b):
  for i in range(1, b+1):
    if b % i == 0:
      print(i)


if __name__ == '__main__':
  b = input("You Number Please: ")
  b = float(b)
  
  if b > 0 and b.is_integer():
    factors(int(b))
  else:
    print("Please enter a positive integer")
