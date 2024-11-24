import os

ARQUIVO = 'SPED.db'
ENCODING_UTF = 'utf-8'
ENCODING_ISO = 'ISO-8859-1'

if os.name == "nt":
    TEMPLATE = 'Dados\\Reg{}.csv'
else:
    TEMPLATE = 'Dados/Reg{}.csv'
    
DELIMITER_COMA = ','
DELIMITER_DOT = ';'

loja = '2'
mes = '07'
ano = '2023'