import shutil
from os import listdir
from os.path import isfile, join, basename


def move(path_origem, path_destino, ext='zip'):
    for item in [join(path_origem, f) for f in listdir(path_origem) if isfile(join(path_origem, f)) and f.endswith(ext)]:
        #print(item)
        shutil.move(item, join(path_destino, basename(item)))
        print('moved "{}" -> "{}"'.format(item,join(path_destino, basename(item))))


if __name__ == '__main__':
    move('/tmp/a', '/tmp/b')
