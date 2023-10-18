# O usuário deve informar de qual número ele deseja ver a tabuada
num = int(input("Informe o número para a tabuada (de 1 a 10): "))

# Verifica se o número está dentro do intervalo permitido
if 1 <= num <= 10:
    print(f"Tabuada de {num}:")

    # Loop de 1 a 10 para gerar a tabuada
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} X {i} = {resultado}")
else:
    print("Número fora do intervalo permitido. Por favor, informe um número de 1 a 10.")

