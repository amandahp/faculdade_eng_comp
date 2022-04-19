'''
  Even-Odd Vending Machine
'''
def odd_or_even(a):
  if a % 2 == 0:
    print("Even")
  else:
    print("Odd")

def print_num(a):
  for i in range(a, a+20, 2):
    print(i)
  

if __name__ == '__main__':
  num = float(input('Enter the number: '))
  if num.is_integer():
    odd_or_even(num)
    print_num(int(num))
  else:
    print("Invalid number")