'''
  Converting temperature from Fahrenheit to Celsius
'''

F = float(input('Enter a temperature: '))
c = (F - 32) * (5/9)
print(f'Temperature in Celsius: {c}')

'''
  Converting temperature from Celsius to Fahrenheit
'''

C = float(input('Enter a temperature: '))
f = C * (9/5) + 32
print(f'Temperature in Fahrenheit: {f}')


'''
  Unit converter: Miles and Kilometers
'''

def print_menu():
  print('1. Kilometers to Miles')
  print('2. Millimeters to Kilometers')


def km_miles():
  km = float(input('Enter distance in kilometers: '))
  miles = km/1.609
  
  print(f'Distance in Miles: {miles}')
  

def miles_km():
  miles = float(input('Enter distance in miles: '))
  km = miles*1.609 
  
  print(f'Distance in Kilometers: {km}')
  

if __name__ == '__main__':
  print_menu()
  choice = input('Which conversion would you like to do: ')
  
  if choice == '1':
    km_miles()
  
  if choice == '2':
    miles_km()