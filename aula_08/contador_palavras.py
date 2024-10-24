def contarPalavra(texto):
    branco = 0
    for caracter in texto:
        if(caracter == " "):
            branco = +1
        
    resposta = len(texto) - branco
    
    return resposta


controlador = True

while controlador:
    palavra = input("Informe o texto a ser contado (ou digite 'sair' para encerrar): ")
    
    if(palavra != "sair"):
        contagem = contarPalavra(palavra)
        print("O total de caracteres no texto informado é: " + str(contagem))
    else:
        controlador = False
        print("Saindo do Programa")