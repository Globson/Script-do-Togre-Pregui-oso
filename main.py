import shutil
import os
import hashlib
from os import listdir
from os.path import isfile, join, basename


def move(path_item, path_destino, ext='pdf'):
    shutil.move(path_item, join(path_destino, basename(path_item)))
    print('moved "{}" -> "{}"'.format(path_item,join(path_destino, basename(path_item))))

def duplicados(path, extension):
    ret = {}

    # Para cada arquivo no diretorio
    for filename in os.listdir(path):

        # Somente arquivos com a extensão desejada
        if filename.endswith(extension):

            # Monta o caminho completo do arquivo
            fullpath = os.path.abspath(os.path.join(path, filename))

            # Calcula o hash MD5 (assinatura) do arquivo
            with open(fullpath, 'rb') as f:
                md5sum = hashlib.md5(f.read()).hexdigest()

            # Adiciona arquivo em um dicionario de listas
            # no qual a chave eh a assinatura do arquivo
            if md5sum not in ret:
                ret[md5sum] = []
            ret[md5sum].append(fullpath)

    for v in ret.items():
        trava = False
        #print(v)
        for k in v:
            if len(k) > 1:
                if not trava:
                    trava = True
                else:
                    del(k[0])
                    for i in k:
                        move(i,'./Repetidos')
    #return {k: v for k, v in ret.items() if len(v) > 1}


#print(duplicados(path='./Pasta', extension='.pdf'))




if __name__ == '__main__':
    #move('/home/grobs/Documentos/Script do togre preguiçoso/Pasta/60b500af9d903.pdf', './Pasta2')
    #print(duplicados(path='./Pasta', extension='.pdf'))
    duplicados(path='./Certificados', extension='.pdf')
    
