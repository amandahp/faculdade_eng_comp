'''
  Enhanced Unit Converter
'''

def print_menu():
  print('1. Converte from Celsius to Fahrenheit or from Fahrenheit to Celsius')
  print('2. Converte from kilograms to pounds or from pounds to kilograms')
  print('3. Converte from kilometers to miles or from miles to kilometers')

  
def converte_temperature():
  print('1. Converte from Celsius to Fahrenheit')
  print('2. Converte from Fahrenheit to Celsius')
  
  option = input('Enter a option (1/2): ')
  
  if option == '1':
    C = float(input('Enter a temperature: '))
    f = C * (9/5) + 32
    print(f'Temperature in Fahrenheit: {f}°F')

  if option == '2':
    F = float(input('Enter a temperature: '))
    c = (F - 32) * (5/9)
    print(f'Temperature in Celsius: {c}°C')


def converte_mass():
  print('1. Converte from kilogram to pound')
  print('2. Converte from pound to kilogram')
  
  option = input('Enter a option (1/2): ')
  
  if option == '1':
    K = float(input('Enter a value: '))
    p = K * 2.20
    print(f'The mass in pound(s) is: {P}lb')
    
  if option == '2':
    P = float(input('Enter a value: '))
    k = P / 2.20
    print(f'The mass in kilogram(s) is: {k}kg')

def converte_distance():
  print('1. Converte from kilometers to miles')
  print('2. Converte from miles to kilometers')

  option = input('Enter a option(1/2):  ')
  
  if option == '1':
    Km = float(input('Enter a value: '))
    mi = Km * 0.6214
    print(f'The distance in mile(s) is: {mi}mile(s)')
  
  if option == '2':
    Mi = float(input('Enter a value: '))
    km = Mi / 0.6214
    print(f'The distance in kilometers(s) is: {km}km')


if __name__ == '__main__':
  print_menu()
  
  opt = input('Enter a option (1/2/3): ')
  
  if opt == '1':
    converte_temperature()
  
  if opt == '2':
    converte_mass()
  
  if opt == '3':
    converte_distance()