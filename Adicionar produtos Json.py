import json

# Função Lambda para calcular o ICMS (18% do valor do produto)
calcular_icms = lambda valor: round(valor * 0.18, 2)

# Função principal
def cadastrar_produtos():
    produtos = []  # Lista para armazenar os produtos

    while True:
        try:
            # Solicita as informações do produto ao usuário
            descricao = input("Digite a descrição do produto: ")
            valor = float(input("Digite o valor do produto (em R$): "))
            embalagem = input("Digite o tipo de embalagem: ")

            # Calcula o ICMS
            icms = calcular_icms(valor)

            # Adiciona o produto à lista
            produto = {
                "descricao": descricao,
                "valor": valor,
                "embalagem": embalagem,
                "icms": icms
            }
            produtos.append(produto)

            # Pergunta se o usuário deseja cadastrar outro produto
            continuar = input("Deseja cadastrar um novo produto? (sim/não): ").strip().lower()
            if continuar != "sim":
                break

        except ValueError:
            print("Erro: O valor do produto deve ser numérico. Tente novamente.")
        except Exception as e:
            print(f"Erro inesperado: {e}. Tente novamente.")

    # Verifica se há pelo menos 5 produtos cadastrados
    if len(produtos) < 5:
        print("Você precisa cadastrar pelo menos 5 produtos.")
        return

    # Gera o arquivo JSON com as informações dos produtos
    try:
        with open("1_5_arquivo_produto.json", "w", encoding="utf-8") as arquivo:
            json.dump(produtos, arquivo, ensure_ascii=False, indent=4)
        # Arquivo gerado com sucesso
        print("Arquivo '1_5_arquivo_produto.json' gerado com sucesso!")
    except Exception as e:
        print(f"Erro ao gerar o arquivo JSON: {e}")

# Executa o programa
if __name__ == "__main__":
    cadastrar_produtos()