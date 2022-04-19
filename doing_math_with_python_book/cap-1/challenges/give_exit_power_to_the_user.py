'''
  Prime number
'''

def number_prime(a):
  div = 0
  
  for i in range(1, a+1):
    if a % i == 0:
      div = div + 1
  
  if div == 2:
    print("Prime number")
  else:
    print("Not prime number")

if __name__ == '__main__':
  while True:
    a = int(input("Enter a number: "))
    number_prime(a)
    
    answer = input("Do you want to exit the program? (y/n) ")
    if answer == 'y':
      break