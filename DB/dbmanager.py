from pathlib import Path
import os
import sqlite3
import csv
from Ferramentas.arquivos import ArquivoExiste
import SPED.dicionarios as dic
import SPED.SPED as SPED
import DB.Queries.DropAndCreate as dc
import DB.Queries.Insert as ins
import DB.Queries.Update as update
import config as cfg

id = ''
nlinha = ''
idPai = ''
produtoPai = ''
particPai = ''

class DB:
    def __init__(self) -> None:
        pass

    def __criabanco(self):
        if ArquivoExiste(cfg.ARQUIVO):
            os.remove(cfg.ARQUIVO)
            Path(cfg.ARQUIVO).touch()
            print("Apagando e recriando o banco")

    @classmethod
    def insereDados(self):
        for registro in SPED.registros:
            self.__insere_registro(self,nlinha,registro,idPai,produtoPai)
            self.__altera_registro(self,registro)
        
        
        self.__insere_outros_dados()
        
    def __insere_registro(self, nlinha, registro, idPai, produtoPai):
        if registro == "0000":
            self.__criabanco(self)

        print("Gravando dados do registro {} no banco de dados".format(registro))

        if ArquivoExiste(cfg.TEMPLATE.format(registro)):
            with open(cfg.TEMPLATE.format(registro) , 'r', encoding=cfg.ENCODING_ISO) as csvfile:
                # create the object of csv.reader()
                csv_file_reader = csv.reader(csvfile, delimiter=cfg.DELIMITER_COMA)
                # skip the header 
                next(csv_file_reader,None)

                reg = {}
                
                connection = sqlite3.connect(cfg.ARQUIVO)
                cursor = connection.cursor()

                cursor.execute(dc.drop_table(registro))
                cursor.execute(dc.create_table(registro))

                for linha in csv_file_reader:

                    for i in range(len(linha)):
                        reg = dic.retorna_dict(None, nlinha, linha, registro, idPai, produtoPai, particPai, dic.TIPO_DB)
                    
                    #print(reg)
                    #print(registro)
                    cursor.execute(ins.insert_data(registro, reg))

                connection.commit()
                connection.close()

    def __altera_registro(self, registro):
        print("Alterando dados do registro {} no banco de dados".format(registro))
        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()


        if not registro in ['0000', '0100', '0150', '0175', '0190', '0205', '0400', 'C113']:
            try:
                cursor.execute(update.update_data(registro))
            except:
                pass

        connection.commit()
        connection.close()

    def __insere_outros_dados():
        tabelas = [
            'TB_INF_ADIC_VL_DECL_52',
            'TB_MOT_REST_57',
            'TB_PAISES_321',
            'TB_MODELOS_411',
            'TB_SIT_NFE_412',
            'TB_GENEROS_421',
            'TB_CST_ICMS_431',
            'TB_CST_IPI_432',
            'TB_CEST',
            'TB_CFOP',
            'TB_CIDADES']
        
        dados = 'Dados/Outros/dados.sql'

        connection = sqlite3.connect(cfg.ARQUIVO)
        cursor = connection.cursor()
        
        for tabela in tabelas:
            print("inserindo dados da tabela {}".format(tabela))
            cursor.execute(dc.drop_other(tabela))
            cursor.execute(dc.create_other(tabela))

        with open(dados, 'r') as f:
            lines = f.readlines()

            for line in lines:
                if line != '':
                    cursor.execute(line)

        connection.commit()
        connection.close()
