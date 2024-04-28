def somaDosAntecessores(numero):
    soma = 0
    for antecessor in range(0, numero):
        soma += antecessor
    return soma

numero = 6
resultado = somaDosAntecessores(numero)
print(f"A soma dos antecessores de {numero} é: {resultado}")