def diferenca_de_quadrados():
  lista_termos = []
  elevado = "^2"
  termo = input("Insira o termo que deseja fatorar: ")
  
  for valores in termo.split():
    lista_termos.append(valores)
    
  if lista_termos[0].count(elevado) == 0:
    termo_1 = lista_termos[0]
    if termo_1.isdigit():
      raiz_1 = int(int(termo_1)**0.5)
    else:
      raiz_1 = termo_1
  else:
    termo_1 = lista_termos[0]
    termo_1 = termo_1.replace('^2', '')
    if termo_1.isdigit():
      raiz_1 = (int(termo_1)**2)**0.5
    else:
      raiz_1 = termo_1
  
   
  if lista_termos[-1].count(elevado) == 0:
    termo_2 = lista_termos[-1]
    if termo_2.isdigit():
      raiz_2 = int(termo_2)**0.5
    else:
      raiz_2 = termo_2
  else:
    termo_2 = lista_termos[-1]
    termo_2 = termo_2.replace('^2', '')
    if termo_2.isdigit():
      raiz_2 = int((int(termo_2)**2)**0.5)
    else:
      raiz_2 = termo_2
  
  print(f'A fatoração do valor {termo} é: \n ({raiz_1} + {raiz_2}) * ({raiz_1} - {raiz_2})')



diferenca_de_quadrados()
  