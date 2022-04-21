import sympy as s
from sympy import factor


def type_base(value_base):
    try:
        return int(value_base)
    except ValueError:
        return s.var(value_base)


def fetch_input():
    n = 1
    list_base = list()
    list_exponent = list()
    while n >= 1:
        base = input(f'Digite o valor da base {n}: ')
        exponent = int(input(f'Digite o valor do expoente {n}: '))
        list_base.append(base)
        list_exponent.append(exponent)
        n = n + 1
        if n > 2:
            answer = input("Deseja adicionar mais valores? (s/n) ").lower()
            if answer == 'n' or answer == 'não':
                break
    return list_base, list_exponent


if __name__ == '__main__':
    print('''
        Bem-Vindo! Siga as instruções para realizar a fatoração do polinômio.
    ''')
    values_poly = fetch_input()
    values_base = values_poly[0]
    values_exponent = values_poly[1]
    new_base = list()
    equation = list()

    for base in values_base:
        base_type = type_base(base)
        new_base.append(base_type)

    for i in new_base:
        for j in values_exponent:
            equation.append(i**j)
            break

    len_eq = len(equation)

    for i in range(0, len_eq):
        if i < (len_eq - 1):
            result = (factor(equation[i] - equation[i+1]))

    print(result)


