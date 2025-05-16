# Solicita o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Solicita o percentual de desconto
desconto = float(input("Digite o desconto (%): "))

# Verifica se o desconto é válido
if 0 <= desconto <= 100:
    valor_desconto = (desconto / 100) * preco
    preco_final = preco - valor_desconto

    print(f"\nDesconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")
else:
    print("Valor de desconto inválido! Deve estar entre 0% e 100%.")
