'''
  Enhanced Multiplication Table Generator
'''


def multi_table(a, b):
  for i in range(1, int(b+1)):
    print(f'{int(a)} x {i} = {int(a*i)}')

if __name__ == '__main__':
  a = float(input("Enter a number: "))
  b = float(input("Enter the amount of multiples: "))
  
  if a.is_integer() and b.is_integer():
    multi_table(a, b)
  else:
    print("Invalid number")
  
