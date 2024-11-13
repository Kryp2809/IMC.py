def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Lista para armazenar os resultados
resultados = []

# Loop para calcular o IMC de várias pessoas
while True:
    peso = float(input("Digite o seu peso em kg (ou 0 para sair): "))
    if peso == 0:
        break
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    categoria = classificar_imc(imc)

    resultados.append((peso, altura, imc, categoria))
    print(f"Seu IMC é {imc:.2f} e você está na categoria: {categoria}")

# Imprimir todos os resultados (opcional)
print("\nResultados de todos os cálculos:")
for peso, altura, imc, categoria in resultados:
    print(f"Peso: {peso}kg - Altura: {altura}m - IMC: {imc:.2f} - Categoria: {categoria}")