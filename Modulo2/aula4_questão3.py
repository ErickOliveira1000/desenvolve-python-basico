# Leitura de dados (entrada)

produto1 = str(input("\033[3m Digite o nome do produto 1: \033[m"))
preco_produto1 = float(input("\033[3m Digite o preço unitário do produto 1: \033[m"))
quantidade_produto1 = int(input("\033[3m Digite a quantidade do produto 1: \033[m"))

produto = str(input("\033[3m igite o nome do produto 2: \033[m"))
preco_produto2 = float(input("\033[3m Digite o preço unitário do produto 2: \033[m"))
quantidade_produto2  = int(input("\033[3m Digite a quantidade do produto 2: \033[m"))

produto = str(input("\033[3m Digite o nome do produto 3: \033[m"))
preco_produto3 = float(input("\033[3m Digite o preço unitário do produto 3: \033[m"))
quantidade_produto3 = int(input("\033[3m Digite a quantidade do produto 3: \033[m"))

# Processamento

# multiplicar o preço pela quantidade do produto
# somar o valor resultante dos produtos

valor = (preco_produto1 * quantidade_produto1) + (preco_produto1 * quantidade_produto1) + (preco_produto1 * quantidade_produto1)

# Saída

print(f"Total:R${valor:,.2f}")
