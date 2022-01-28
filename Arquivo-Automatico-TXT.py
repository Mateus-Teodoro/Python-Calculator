# import os

nomeArquivo = input('Digite o diretório do arquivo:')
nomeArquivo += '.txt'
arquivo = open(nomeArquivo, 'w')


texto = input("Digite o texto do arquivo:")

arquivo.write(texto)
arquivo.close()

abrir = input('Deseja abir o arquivo para leitura? ')
if abrir.capitalize() == 'Sim':
    opfile = open(nomeArquivo, 'r', encoding='utf8')
    conteudo = opfile.read()
    opfile.close()
    list(conteudo)
    print(conteudo)
else:
    print('Conteúdo gravado com sucesso!')
