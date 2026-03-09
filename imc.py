peso = float(input("Digite seu peso "))
altura = float(input("Digite sua altura "))

imc = peso / (altura ** 2)
print(f"Seu imc: {imc:.4f}")
if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("OBS 1")
elif imc < 40:
    print("OBS 2")
else:
    print("OBS 3")