'''
  Programa que gera um número aleatório entre 0 e 10...
'''

import random

if __name__ == '__main__':
  
  num_gerado = random.randint(0, 10)
  num_adivinhado = 0
  
  while num_adivinhado != num_gerado:
    num_adivinhado = int(input("Digite um número de 0 a 10: "))
  
  print('Parabéns, você adivinhou o número!')
  print(f'Número gerado: {num_gerado}')