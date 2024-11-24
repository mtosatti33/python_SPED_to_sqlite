from DB.dbmanager import DB
from SPED.SPED import SPED
import Ferramentas.arquivos as arquivos
import config as cfg

GERA_CSV = False
GERA_MULTIPLA = True

if __name__ == "__main__":
    #Compacta pasta para backup antes de apagar
    #arquivos.compactar_pasta("CSV/")

    if GERA_CSV:
        #Apaga arquivos CSV antes de serem gerados
        arquivos.ApagarArquivosCSV()

        if not GERA_MULTIPLA:
            arquivo=arquivos.listar_arquivo(cfg.loja, cfg.mes, cfg.ano)
            
            if not arquivos.ArquivoExiste(arquivo):
                print('Arquivo SPED não encontrado')
                quit()

            SPED.ler_arquivo(1, arquivo)
        else:
            i = 1
            for arquivo in arquivos.listar_arquivos():
                SPED.ler_arquivo(i, arquivo)
                i += 1
    
    arquivos.tratar_erro_registro_0150()
    arquivos.tratar_erro_registro_0205()

    DB.insereDados()
    