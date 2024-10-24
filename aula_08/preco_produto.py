def classificarProduto(preco):
    if(preco < 50):
        resposta = "Produto de preço baixo"
    elif(preco > 100):
        resposta = "Produto de preço alto"
    else:
        resposta = "Produto de preço médio"
    return resposta

nomeProduto = input("Informe o nome do Produto: ")
precoProduto = int(input("Informe o preço do produto: "))
texto = classificarProduto(precoProduto)

print("Produto: " + nomeProduto + " Valor: R$ " + str(precoProduto) + " " + texto)