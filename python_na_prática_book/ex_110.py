'''
  Escreva um programa que executa um bloco de código situado dentro de um 
  comentário
'''

if __name__ == '__main':
  codigo = '''
  num = int(input("Digite um número: "))
  print(f'O seu número elevado ao quadrado é: {num**2}')
  '''
  
  exec(codigo)