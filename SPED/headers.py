from pathlib import Path
import os
from csv import DictWriter

#bloco0
_0000 = ['ID', 'REG', 'COD_VER', 'COD_FIN', 'DT_INI', 'DT_FIN', 'NOME', 
         'CNPJ', 'CPF', 'UF', 
         'IE', 'COD_MUN', 'IM', 'SUFRAMA', 'IND_PERFIL', 'IND_ATIV', 'NLINHA']

_0100 = ['ID', 'REG', 'NOME', 'CPF', 'CRC', 'CNPJ', 'CEP', 
         'END', 'NUM', 'COMPL', 'BAIRRO', 'FONE', 'FAX', 
         'EMAIL', 'COD_MUN', 'NLINHA']

_0150 = ['ID', 'REG', 'COD_PART', 'NOME', 'COD_PAIS', 
         'CNPJ', 'CPF', 
         'IE', 'COD_MUN', 'SUFRAMA', 'END', 'NUM', 'COMPL', 'BAIRRO', 'NLINHA']

_0175 = ['ID', 'REG', 'DT_ALT', 'NR_CAMPO', 'CONT_ANT', 'ID_PAI', 'NLINHA']

_0190 = ['ID', 'REG', 'UNID', 'DESCR', 'NLINHA']

_0200 = ['ID', 'REG', 'COD_ITEM', 'DESCR_ITEM', 'COD_BARRA', 
         'COD_ANT_ITEM', 'UNID_INV', 'TIPO_ITEM', 
         'COD_NCM', 'EX_IPI', 'COD_GEN', 'COD_LST', 'ALIQ_ICMS', 'CEST', 'NLINHA']

_0205 = ['ID', 'REG', 'DESCR_ANT_ITEM', 'DT_INI', 'DT_FIM', 'COD_ANT_ITEM', 'ID_PAI', 'NLINHA']

_0220 = ['ID', 'REG', 'UNID_CONV', 'FAT_CONV', 'COD_BARRA', 'ID_PAI', 'NLINHA']

_0400 = ['ID', 'REG', 'COD_NAT', 'DESCR_NAT', 'NLINHA']



#blocoC
_C100 = ['ID', 'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 
         'NUM_DOC', 'CHV_NFE', 'DT_DOC', 'DT_E_S', 'VL_DOC', 'IND_PGTO', 
         'VL_DESC', 'VL_ABAT_NT', 'VL_MERC', 'IND_FRT', 'VL_FRT', 'VL_SEG', 'VL_OUT_DA', 
         'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 
         'VL_IPI', 'VL_PIS', 'VL_COFINS', 'VL_PIS_ST', 'VL_COFINS_ST', 'NLINHA']

_C112 = ['ID', 'REG', 'COD_DA', 'UF', 'NUM_DA', 'COD_AUT', 'VL_DA', 'DT_VCTO', 'DT_PGTO', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']

_C113 = ['ID', 'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'SER', 'SUB', 'NUM_DOC', 'DT_DOC', 'CHV_DOCe', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']

_C170 = ['ID', 'REG', 'NUM_ITEM', 'COD_ITEM', 'DESCR_COMPL', 'QTD', 'UNID', 'VL_ITEM', 'VL_DESC', 'IND_MOV', 'CST_ICMS', 'CFOP', 'COD_NAT', #13
         'VL_BC_ICMS', 'ALIQ_ICMS', 'VL_ICMS', 'VL_BC_ICMS_ST', 'ALIQ_ST', 'VL_ICMS_ST', #6
         'IND_APUR', 'CST_IPI', 'COD_ENQ', 'VL_BC_IPI', 'ALIQ_IPI', 'VL_IPI', #6
         'CST_PIS', 'VL_BC_PIS', 'ALIQ_PIS_PCT', 'QUANT_BC_PIS', 'ALIQ_PIS_RS', 'VL_PIS', #6
         'CST_COFINS', 'VL_BC_COFINS', 'ALIQ_COFINS_PCT', 'QUANT_BC_COFINS', 'ALIQ_COFINS_RS', 'VL_COFINS', 'COD_CTA', 'VL_ABAT_NT', 'PARTIC_PAI', 'ID_PAI', 'NLINHA'] #10

_C180 = ['ID', 'REG', 'COD_RESP_RET', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_BC_ICMS_ST_CONV', 'VL_UNIT_ICMS_ST_CONV', 
         'VL_UNIT_FCP_ST_CONV', 'COD_DA', 'NUM_DA', 'PRODUTO_PAI', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']

_C181 = ['ID', 'REG', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'COD_MOD_SAIDA', 'SERIE_SAIDA', 'ECF_FAB_SAIDA', 'NUM_DOC_SAIDA', 'CHV_DFE_SAIDA', 'DT_DOC_SAIDA', 'NUM_ITEM_SAIDA', 
         'VL_UNIT_CONV_SAIDA', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA', 
         'VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA', 'VL_UNIT_ICMS_OP_CONV_SAIDA', 'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 
         'VL_UNIT_FCP_ST_CONV_COMPL', 'PRODUTO_PAI', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']

_C185 = ['ID', 'REG', 'NUM_ITEM', 'COD_ITEM', 'CST_ICMS', 'CFOP', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'VL_UNIT_CONV', 
         'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_CONV_REST', 
         'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']

_C186 = ['ID', 'REG', 'NUM_ITEM', 'COD_ITEM', 'CST_ICMS', 'CFOP', 'COD_MOT_REST_COMPL', 'QUANT_CONV', 'UNID', 'COD_MOD_ENTRADA', 'SERIE_ENTRADA', 
         'NUM_DOC_ENTRADA', 'CHV_DFE_ENTRADA', 'DT_DOC_ENTRADA', 'NUM_ITEM_ENTRADA', 
         'VL_UNIT_CONV_ENTRADA', 'VL_UNIT_ICMS_OP_CONV_', 'VL_UNIT_BC_ICMS_ST', 'VL_UNIT_ICMS_ST_CONV_ENTRADA', 'VL_UNIT_FCP_ST_CONV_ENTRADA', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']

_C190 = ['ID', 'REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_BC_ICMS_', 'VL_ICMS_ST', 'VL_RED_BC', 'VL_IPI', 'COD_OBS', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']



#blocoD
_D100 = ['ID', 'REG', 'IND_OPER', 'IND_EMIT', 'COD_PART', 'COD_MOD', 'COD_SIT', 'SER', 'SUB', 'NUM_DOC', 'CHV_CTE', 'DT_DOC', 'DT_A_P', 'TP_CTE', 'CHV_CTE_REF', 
         'VL_DOC', 'VL_DESC', 'IND_FRT', 'VL_SERV', 'VL_BC_ICMS', 'VL_ICMS', 
         'VL_NT', 'COD_INF', 'COD_CTA', 'COD_MUN_ORIG', 'COD_MUN_DEST', 'NLINHA']

_D190 = ['ID', 'REG', 'CST_ICMS', 'CFOP', 'ALIQ_ICMS', 'VL_OPR', 'VL_BC_ICMS', 'VL_ICMS', 'VL_RED_BC', 'COD_OBS', 'PARTIC_PAI', 'ID_PAI', 'NLINHA']



#blocoE
_E110 = ['ID', 'REG', 
         'VL_TOT_DEBITOS', 'VL_AJ_DEBITOS', 'VL_TOT_AJ_DEBITOS', 'VL_ESTORNOS_CRED', 'VL_TOT_CREDITOS', 
         'VL_AJ_CREDITOS', 'VL_TOT_AJ_CREDITOS', 'VL_ESTORNOS_DEB', 'VL_SLD_CREDOR_ANT', 'VL_SLD_APURADO', 
         'VL_TOT_DED', 'VL_ICMS_RECOLHER', 'VL_SLD_CREDOR_TRANSPORTAR', 'DEB_ESP', 'NLINHA']

_E115 = ['ID', 'REG', 'COD_INF_ADIC', 'VL_INF_ADIC', 'DESCR_COMPL_AJ', 'NLINHA']

_E210 = ['ID', 'REG', 'IND_MOV_ST', 'VL_SLD_CRED_ANT_ST', 'VL_DEVOL_ST', 'VL_RESSARC_ST', 'VL_OUT_CRED_ST', 
         'VL_AJ_CREDITOS_ST', 'VL_RETENCAO_ST', 'VL_OUT_DEB_ST', 
         'VL_AJ_DEBITOS_ST', 'VL_SLD_DEV_ANT_ST', 'VL_DEDUCOES_ST', 'VL_ICMS_RECOL_ST', 'VL_SLD_CRED_ST_TRANSPORTAR', 'DEB_ESP_ST', 'NLINHA']



#blocoH
_H010 = ['ID', 'REG', 'COD_ITEM', 'UNID', 'QTD', 'VL_UNIT', 'VL_ITEM', 'IND_PROP', 'COD_PART', 'TXT_COMPL', 'COD_CTA', 'VL_ITEM_IR', 'NLINHA']

_H030 = ['ID', 'REG', 'VL_ICMS_OP', 'VL_BC_ICMS_ST', 'VL_ICMS_ST', 'VL_FCP', 'ID_PAI', 'NLINHA']



#bloco1
_1250 = ['ID', 'REG', 'VL_CREDITO_ICMS_OP', 'VL_ICMS_ST_REST', 'VL_FCP_ST_REST', 'VL_ICMS_ST_COMPL', 'VL_FCP_ST_COMPL', 'NLINHA']

_1255 = ['ID', 'REG', 'COD_MOT_REST_COMPL', 'VL_CREDITO_ICMS_OP_MOT', 
         'VL_ICMS_ST_REST_MOT', 'VL_FCP_ST_REST_MOT', 
         'VL_ICMS_ST_COMPL_MOT', 'VL_FCP_ST_COMPL_MOT', 'NLINHA']

_1601 = ['ID', 'REG', 'COD_PART_IP', 'COD_PART_IT', 'TOT_VS', 'TOT_ISS', 'TOT_OUTROS', 'NLINHA']

def defineCabecalho(registro):
        header = []
        if registro == '0000':
            header = _0000
        if registro == '0100':
            header = _0100
        if registro == '0150':
            header = _0150
        if registro == '0175':
            header = _0175
        if registro == '0190':
            header = _0190
        if registro == '0200':
            header = _0200
        if registro == '0205':
            header = _0205
        if registro == '0220':
            header = _0220
        if registro == '0400':
            header = _0400
        if registro == 'C100':
            header = _C100
        if registro == 'C112':
            header = _C112
        if registro == 'C113':
            header = _C113
        if registro == 'C170':
            header = _C170
        if registro == 'C180':
            header = _C180
        if registro == 'C181':
            header = _C181
        if registro == 'C185':
            header = _C185
        if registro == 'C186':
            header = _C186
        if registro == 'C190':
            header = _C190
        if registro == 'D100':
            header = _D100
        if registro == 'D190':
            header = _D190
        if registro == 'E110':
            header = _E110
        if registro == 'E115':
            header = _E115
        if registro == 'E210':
            header = _E210
        if registro == 'H010':
            header = _H010
        if registro == 'H030':
            header = _H030
        if registro == '1250':
            header = _1250
        if registro == '1255':
            header = _1255
        if registro == '1601':
            header = _1601

        return header

def GeraCabecalho(arquivo, header):
    if not os.path.exists(arquivo):
        Path(arquivo).touch()
        with open(arquivo, 'a+', newline='', encoding='utf-8') as f:
            dr = DictWriter(f, fieldnames=header)
            dr.writeheader()