import os, zipfile


def show_file_size_and_compress(size):
    kb = size/1024
    mb = kb/1024
    gb = mb/1024
    print('\nO tamanho original do arquivo é:')
    print('Bytes: {}'.format (size))
    print('Kilobytes (KB): {0:.2f}'.format(kb))
    print('Megabytes (MB): {0:.2f}'.format (mb))
    print('Gigabytes (GB): {0:.2f}'.format (gb))
   
file_path = str(input(r'Insira o caminho do arquivo a ser verificado: '))
size =  os.path.getsize(file_path)

if size > 10000000:
    print('Arquivo maior que 10MB será necessário compacta-lo, siga as instruções abaixo.\n')
    print('Informe o caminho de destino do arquivo, nome e extensão(.zip).')
    print('Ex.: c:\pasta_de_destino\arquivo.zip\n')
    arquivo_zip = zipfile.ZipFile(str(input('Informe o caminho e nome do arquivo: ')), 'w')
    arquivo_zip.write(file_path, compress_type = zipfile.ZIP_DEFLATED)
    arquivo_zip.close()
    print('\nArquivo compactado com SUCESSO.') 

if __name__ == '__main__':
    show_file_size_and_compress(size)