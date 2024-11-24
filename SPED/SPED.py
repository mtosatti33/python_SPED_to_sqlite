from csv import DictWriter
import SPED.headers as headers
import SPED.dicionarios as dic
import Ferramentas.arquivos as arquivos
import config as cfg
import re

registros = ['0000', '0100', '0150', '0175', '0190', '0200', '0205', '0220', '0400', 
             'C100', 'C112', 'C113', 'C170', 'C180', 'C181', 'C185', 'C186', 'C190',
             'D100', 'D190',
             'E110', 'E115', 'E210',
             'H010', 'H030',
             '1250', '1255', '1601']

class SPED():
    def __init__(self) -> None:
        pass

    @classmethod
    def ler_arquivo(self, id, arquivo):

        f = open(arquivo, "r", encoding=cfg.ENCODING_ISO)
        idPai = ''
        produtoPai = ''
        particPai = ''
        nlinha = 1
        for i in f:
            x = re.split("\|", i)
            if x[1] in registros:
                if x[1] == "0150" or x[1] == "0200" or x[1] == "H010":
                    idPai = x[2]
                if x[1] == "C100":
                    idPai = x[8]
                    particPai = x[4]
                if x[1] == "C170":
                    produtoPai = x[3]
                if x[1] == "D100":
                    idPai = x[9]
                    particPai = x[4]

                self.__gerar_registros(id, nlinha, x, x[1], idPai, produtoPai, particPai)

            nlinha += 1
    
    def __gerar_registros(id, nlinha, linha, registro, idPai, produtoPai, particPai):
        arquivo = cfg.TEMPLATE.format(registro)
        print("Gerando Registro {}".format(registro))
        header = headers.defineCabecalho(registro=registro)
        reg = {}

        headers.GeraCabecalho(arquivo, header)
        with open(arquivo, 'a+', newline='', encoding=cfg.ENCODING_UTF) as f:
            reg = dic.retorna_dict(id, nlinha, linha, registro, idPai, produtoPai, particPai, dic.TIPO_CSV)
            
            dr = DictWriter(f, fieldnames=header)

            dr.writerow(reg)
