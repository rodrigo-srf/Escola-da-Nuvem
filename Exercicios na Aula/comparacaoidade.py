# Solicita a idade
idade = int(input("Digite sua idade: "))

# Condicional
if idade < 0:
    print("Idade inválida! Você é um viajante do tempo? 🌀")
elif idade < 12:
    print("Você é uma criança 👶")
elif idade < 18:
    print("Você é um adolescente 🧒")
elif idade < 60:
    print("Você é um adulto 🧑")
else:
    print("Você é um idoso 👴👵 (experiente, claro!)")