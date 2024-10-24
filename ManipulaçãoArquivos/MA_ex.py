'''
Usos:
Armazenar dados de forma persistente
Criar arquivos de log
Integrar diferentes aplicações
'''

'''
open () -> Abrir arquivos
caminho e nome do arquivo
modo de abertura

r -> abre um arquivo existente para leitura | se não for localizado, irá gerar uma exceção
w -> Abre um arquivo para uma operação de escrita de dados | Se o arquivo já existir, será substituido | Se o arquivo não existir, será criado
a -> Abre um arquivo para operação de anexar dados | Se o arquivo existir, ele não será substituido | Se o arquivo não existir, será criado
'''

#arquivo = open('nomearquivo.txt', 'r')

'''
Leitura de arquivos
Ler o conteúdo de um arquivo e copiar para uma string
'''
arquivo = open(r'ManipulaçãoArquivos\arquivo.txt', 'r') #será aberto para leitura | r antes para caracteres especiais

texto = arquivo.read() #a função read() irá copiar todo o arquivo pra string
print(texto)

arquivo.close() #Fecha o arquivo e libera a memória

'''
Leitura de arquivos
Ler o conteúdo de um arquivo e utilizar o loop pra percorrer cada linha
'''

arquivo = open(r'ManipulaçãoArquivos\arquivo.txt', 'r')

#O for irá percorrer cada linha do arquivo
for linha in arquivo:
    print(linha)

arquivo.close()

'''
Escrita de arquivos
Criar um arquivo e escrever um texto no arquivo criado
'''

#O arquivo será criado/sobrescrito e aberto para escrita
arquivo = open(r'ManipulaçãoArquivos\arquivoescrita1.txt', 'w')

#Escreve uma string no arquivo com a função write()
arquivo.write('Este texto será escrito no arquivo')

arquivo.close()

'''
Escrita de arquivos
Cria um arquivo e escreve dados informados pelo usuario
'''

arquivo = open(r'ManipulaçãoArquivos\arquivoescrita2.txt', 'w')

nome = input('Digite seu nome: ')
arquivo.write(nome + '\n')

idade = int(input('Escreva sua idade: '))
arquivo.write(str(idade) + '\n')

arquivo.close

'''
Escrita de arquivos
Adicionar um texto existente
'''

arquivo = open(r'ManipulaçãoArquivos\arquivoescrita3.txt', 'a')

arquivo.write('Este texto será escrito no arquivo\n')

arquivo.close

