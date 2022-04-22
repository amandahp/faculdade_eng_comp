import math


def formatting(coe, expo, term):
    exponent = f'^{expo}'
    coefficient = f'{coe}{term}{expo}'

    if coe == 0:
        coefficient = ''
    if coe == 1:
        coefficient = f'{term}{exponent}'
    if expo == 1:
        coefficient = f'{term}'
    if expo == 0:
        coefficient = ''

    return coefficient


def binomial_theorem(co_a, co_b, n):
    list_combination = list()
    list_terms = list()
    n_f = n
    k = 0
    polynomial = " "
    for i in range(0, n+1):
        combination = math.comb(n, i)
        list_combination.append(combination)

    for c in list_combination:
        term_a = formatting(co_a, n_f, 'a')
        term_b = formatting(co_b, k, 'b')

        if c > 1:
            term = f'{c}{term_a}{term_b}'
        else:
            term = f'{term_a}{term_b}'

        n_f = n_f - 1
        k = k + 1
        list_terms.append(term)

    for j in range(0, (len(list_terms)+1)):
        if j < (len(list_terms)):
            polynomial = polynomial + " " + list_terms[j]
        if j < (len(list_terms)-1):
            polynomial = polynomial + " +"

    return polynomial


if __name__ == '__main__':
    print('''
        Binômio de Newton
        ------------------
    (a+b)ⁿ = ⁿΣr(n, r) a^k b^n-k
    ''')
    co_a = int(input("Insira o valor do coeficiente a: "))
    co_b = int(input("Insira o valor do coeficiente b: "))
    n = int(input("Insira o valor do expoente n: "))
    print(binomial_theorem(co_a, co_b, n))
