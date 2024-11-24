import pandas as pd
import os
import glob
import config as cfg
import shutil

csvfile = None

def ApagarArquivosCSV():
    if os.name == "nt":
        path = "Dados\\"
    else:
        path = "Dados/"
        
    for arquivo in os.listdir(path):
        try:
            os.remove(path + arquivo)
        except PermissionError:
            pass
        except IsADirectoryError:
            pass

def SalvarParaCSV(lista, reg):
    df = pd.json_normalize(lista, errors='ignore')

    if os.name == "nt":
        #Windows
        df.to_csv('CSV\\Reg{}.csv'.format(reg), sep=cfg.DELIMITER_DOT, encoding=cfg.ENCODING_UTF, index=False)
    else:
        #Linux
        df.to_csv('CSV/Reg{}.csv'.format(reg), sep=cfg.DELIMITER_DOT, encoding=cfg.ENCODING_UTF, index=False)

def ArquivoExiste(arquivo):
    return os.path.exists(arquivo)

def listar_arquivos():
    if os.name == "nt":
        return glob.glob('C:\\Users\\Marcelo\Dropbox\\SPED\\Arquivos SPED\\**\\**\\*.txt', recursive=False)
    else:
        return glob.glob('/home/marcelo/Dropbox/SPED/Arquivos SPED/**/**/*.txt', recursive=False)
    
def listar_arquivo(loja, mes, ano):
    if os.name == 'nt':
    #Windows
        return "C:\\Users\\marcelo\\Dropbox\\SPED\\lj{}_efd{}{}.txt".format(loja, mes, ano)
    else:
        #Linux
        return "/home/marcelo/Dropbox/SPED/lj{}_efd{}{}.txt".format(loja, mes, ano)
    
def compactar_pasta(dir):
    shutil.make_archive(dir, 'zip', dir)

def tratar_erro_registro_0150():
    with open(cfg.TEMPLATE.format('0150'), 'r') as file:
        dados = file.read()

        dados = dados.replace("'", " ")

    with open(cfg.TEMPLATE.format('0150'), 'w') as new_file:
        new_file.write(dados)

def tratar_erro_registro_0205():
    with open(cfg.TEMPLATE.format('0205'), 'r') as file:
        dados = file.read()

        dados = dados.replace("'", " ")

    with open(cfg.TEMPLATE.format('0205'), 'w') as new_file:
        new_file.write(dados)