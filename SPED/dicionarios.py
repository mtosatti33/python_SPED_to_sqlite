
TIPO_CSV = 'csv'
TIPO_DB = 'db'

def retorna_dict(id, nlinha, linha, registro, idPai, produtoPai, particPai, tipo):
    """
    Parâmetros:
        -nlinha: número da linha
        -linha: array de registros
        -registro: registro do SPED
        -idPai: identificador principal
        -particPai: participante do registro C100
        -produtoPai: produto no registro C170

    tipo:
        -csv:   será gerado via CSV
        -db:    será gerado via db
    """
    reg = {}

    if tipo == TIPO_CSV:
        reg['ID'] = id
    elif tipo == TIPO_DB:
        reg['ID'] = linha[0]

    reg['REG'] = linha[1]

    if registro == "0000":
        reg['COD_VER'] = linha[2]
        reg['COD_FIN'] = linha[3]
        reg['DT_INI'] = linha[4]
        reg['DT_FIN'] = linha[5]
        reg['NOME'] = linha[6]
        reg['CNPJ'] = linha[7]
        reg['CPF'] = linha[8]
        reg['UF'] = linha[9]
        reg['IE'] = linha[10]
        reg['COD_MUN'] = linha[11]
        reg['IM'] = linha[12]
        reg['SUFRAMA'] = linha[13]
        reg['IND_PERFIL'] = linha[14]
        reg['IND_ATIV'] = linha[15]

    elif registro == "0100":
        reg['NOME'] = linha[2]
        reg['CPF'] = linha[3]
        reg['CRC'] = linha[4]
        reg['CNPJ'] = linha[5]
        reg['CEP'] = linha[6]
        reg['END'] = linha[7]
        reg['NUM'] = linha[8]
        reg['COMPL'] = linha[9]
        reg['BAIRRO'] = linha[10]
        reg['FONE'] = linha[11]
        reg['FAX'] = linha[12]
        reg['EMAIL'] = linha[13]
        reg['COD_MUN'] = linha[14]

    elif registro == "0150":
        reg['COD_PART'] =  linha[2]
        reg['NOME'] = linha[3]
        reg['COD_PAIS'] = linha[4]
        reg['CNPJ'] = linha[5]
        reg['CPF'] = linha[6]
        reg['IE'] = linha[7]
        reg['COD_MUN'] = linha[8]
        reg['SUFRAMA'] = linha[9]
        reg['END'] = linha[10]
        reg['NUM'] = linha[11]
        reg['COMPL'] = linha[12]
        reg['BAIRRO'] = linha[13]

    elif registro == "0175":
        reg['DT_ALT'] = linha[2]
        reg['NR_CAMPO'] = linha[3]
        reg['CONT_ANT'] =  linha[4]

    elif registro == "0190":
        reg['UNID'] = linha[2]
        reg['DESCR'] = linha[3]

    elif registro == "0200":
        reg['COD_ITEM'] = linha[2]
        reg['DESCR_ITEM'] = linha[3]
        reg['COD_BARRA'] = linha[4]
        reg['COD_ANT_ITEM'] = linha[5]
        reg['UNID_INV'] = linha[6]
        reg['TIPO_ITEM'] = linha[7]
        reg['COD_NCM'] = linha[8]
        reg['EX_IPI'] = linha[9]
        reg['COD_GEN'] = linha[10]
        reg['COD_LST'] = linha[11]
        reg['ALIQ_ICMS'] = linha[12]
        reg['CEST'] = linha[13]

    elif registro == "0205":
        reg['DESCR_ANT_ITEM'] = linha[2]
        reg['DT_INI'] = linha[3]
        reg['DT_FIM'] =  linha[4]
        reg['COD_ANT_ITEM'] = linha[5]

    elif registro == "0220":
        reg['UNID_CONV'] = linha[2]
        reg['FAT_CONV'] = linha[3]
        reg['COD_BARRA'] =  linha[4]

    elif registro == "0400":
        reg['COD_NAT'] = linha[2]
        reg['DESCR_NAT'] = linha[3]
            
    elif registro == "C100":
        reg['IND_OPER'] = linha[2]
        reg['IND_EMIT'] = linha[3]
        reg['COD_PART'] = linha[4]
        reg['COD_MOD'] = linha[5]
        reg['COD_SIT'] = linha[6]
        reg['SER'] = linha[7]
        reg['NUM_DOC'] = linha[8]
        reg['CHV_NFE'] = linha[9]
        reg['DT_DOC'] = linha[10]
        reg['DT_E_S'] = linha[11]
        reg['VL_DOC'] = linha[12]
        reg['IND_PGTO'] = linha[13]
        reg['VL_DESC'] = linha[14]
        reg['VL_ABAT_NT'] = linha[15]
        reg['VL_MERC'] = linha[16]
        reg['IND_FRT'] = linha[17]
        reg['VL_FRT'] = linha[18]
        reg['VL_SEG'] = linha[19]
        reg['VL_OUT_DA'] = linha[20]
        reg['VL_BC_ICMS'] = linha[21]
        reg['VL_ICMS'] = linha[22]
        reg['VL_BC_ICMS_ST'] = linha[23]
        reg['VL_ICMS_ST'] = linha[24]
        reg['VL_IPI'] = linha[25]
        reg['VL_PIS'] = linha[26]
        reg['VL_COFINS'] = linha[27]
        reg['VL_PIS_ST'] = linha[28]
        reg['VL_COFINS_ST'] = linha[29]

    elif registro == "C112":
        reg['COD_DA'] = linha[2]
        reg['UF'] = linha[3]
        reg['NUM_DA'] = linha[4]
        reg['COD_AUT'] = linha[5]
        reg['VL_DA'] = linha[6]
        reg['DT_VCTO'] = linha[7]
        reg['DT_PGTO'] = linha[8]

    elif registro == "C113":
        reg['IND_OPER'] = linha[2]
        reg['IND_EMIT'] = linha[3]
        reg['COD_PART'] = linha[4]
        reg['COD_MOD'] = linha[5]
        reg['SER'] = linha[6]
        reg['SUB'] = linha[7]
        reg['NUM_DOC'] = linha[8]
        reg['DT_DOC'] = linha[9]
        reg['CHV_DOCe'] = linha[10]

    elif registro == "C170":
        reg['NUM_ITEM'] = linha[2] #3
        reg['COD_ITEM'] = linha[3]
        reg['DESCR_COMPL'] = linha[4]
        reg['QTD'] = linha[5] #6
        reg['UNID'] = linha[6]
        reg['VL_ITEM'] = linha[7]
        reg['VL_DESC'] = linha[8] #9
        reg['IND_MOV'] = linha[9]
        reg['CST_ICMS'] = linha[10]
        reg['CFOP'] = linha[11] #12
        reg['COD_NAT'] = linha[12]
        reg['VL_BC_ICMS'] = linha[13]
        reg['ALIQ_ICMS'] = linha[14] #15
        reg['VL_ICMS'] = linha[15]
        reg['VL_BC_ICMS_ST'] = linha[16] 
        reg['ALIQ_ST'] = linha[17] #18
        reg['VL_ICMS_ST'] = linha[18]
        reg['IND_APUR'] = linha[19]
        reg['CST_IPI'] = linha[20] #21
        reg['COD_ENQ'] = linha[21]
        reg['VL_BC_IPI'] = linha[22]
        reg['ALIQ_IPI'] = linha[23] #24
        reg['VL_IPI'] = linha[24]
        reg['CST_PIS'] = linha[25]
        reg['VL_BC_PIS'] = linha[26] #27
        reg['ALIQ_PIS_PCT'] = linha[27]
        reg['QUANT_BC_PIS'] = linha[28] 
        reg['ALIQ_PIS_RS'] = linha[29] #30
        reg['VL_PIS'] = linha[30]
        reg['CST_COFINS'] = linha[31]
        reg['VL_BC_COFINS'] = linha[32] #33
        reg['ALIQ_COFINS_PCT'] = linha[33]
        reg['QUANT_BC_COFINS'] = linha[34]
        reg['ALIQ_COFINS_RS'] = linha[35] #36
        reg['VL_COFINS'] = linha[36]
        reg['COD_CTA'] = linha[37]
        reg['VL_ABAT_NT'] = linha[38] #39

    elif registro == "C180":
        reg['COD_RESP_RET'] = linha[2]
        reg['QUANT_CONV'] = linha[3]
        reg['UNID'] = linha[4]
        reg['VL_UNIT_CONV'] = linha[5]
        reg['VL_UNIT_ICMS_OP_CONV'] = linha[6]
        reg['VL_UNIT_BC_ICMS_ST_CONV'] = linha[7]
        reg['VL_UNIT_ICMS_ST_CONV'] = linha[8]
        reg['VL_UNIT_FCP_ST_CONV'] = linha[9]
        reg['COD_DA'] = linha[10]
        reg['NUM_DA'] = linha[11]

    elif registro == "C181":
        reg['COD_MOT_REST_COMPL'] = linha[2]
        reg['QUANT_CONV'] = linha[3]
        reg['UNID'] = linha[4]
        reg['COD_MOD_SAIDA'] = linha[5]
        reg['SERIE_SAIDA'] = linha[6]
        reg['ECF_FAB_SAIDA'] = linha[7]
        reg['NUM_DOC_SAIDA'] = linha[8]
        reg['CHV_DFE_SAIDA'] = linha[9]
        reg['DT_DOC_SAIDA'] = linha[10]
        reg['NUM_ITEM_SAIDA'] = linha[11]
        reg['VL_UNIT_CONV_SAIDA'] = linha[12]
        reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA'] = linha[13]
        reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA'] = linha[14]
        reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA'] = linha[15]
        reg['VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA'] = linha[16]
        reg['VL_UNIT_ICMS_OP_CONV_SAIDA'] = linha[17]
        reg['VL_UNIT_ICMS_ST_CONV_REST'] = linha[18]
        reg['VL_UNIT_FCP_ST_CONV_REST'] = linha[19]
        reg['VL_UNIT_ICMS_ST_CONV_COMPL'] = linha[20]
        reg['VL_UNIT_FCP_ST_CONV_COMPL'] = linha[21]

    elif registro == "C185":
        reg['NUM_ITEM'] = linha[2]
        reg['COD_ITEM'] = linha[3]
        reg['CST_ICMS'] = linha[4]
        reg['CFOP'] = linha[5]
        reg['COD_MOT_REST_COMPL'] = linha[6]
        reg['QUANT_CONV'] = linha[7]
        reg['UNID'] = linha[8]
        reg['VL_UNIT_CONV'] = linha[9]
        reg['VL_UNIT_ICMS_NA_OPERACAO_CONV'] = linha[10] 
        reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV'] = linha[11]
        reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV'] = linha[12]
        reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV'] = linha[13]
        reg['VL_UNIT_ICMS_ST_CONV_REST'] = linha[14] 
        reg['VL_UNIT_FCP_ST_CONV_REST'] = linha[15]
        reg['VL_UNIT_ICMS_ST_CONV_COMPL'] = linha[16]
        reg['VL_UNIT_FCP_ST_CONV_'] = linha[17]

    elif registro == "C186":
        reg['NUM_ITEM'] = linha[2] 
        reg['COD_ITEM'] = linha[3]
        reg['CST_ICMS'] = linha[4]
        reg['CFOP'] = linha[5]
        reg['COD_MOT_REST_COMPL'] = linha[6]
        reg['QUANT_CONV'] = linha[7]
        reg['UNID'] = linha[8]
        reg['COD_MOD_ENTRADA'] = linha[9]
        reg['SERIE_ENTRADA'] = linha[10]
        reg['NUM_DOC_ENTRADA'] = linha[11]
        reg['CHV_DFE_ENTRADA'] = linha[12]
        reg['DT_DOC_ENTRADA'] = linha[13]
        reg['NUM_ITEM_ENTRADA'] = linha[14]
        reg['VL_UNIT_CONV_ENTRADA'] = linha[15] 
        reg['VL_UNIT_ICMS_OP_CONV_'] = linha[16] 
        reg['VL_UNIT_BC_ICMS_ST'] = linha[17]
        reg['VL_UNIT_ICMS_ST_CONV_ENTRADA'] = linha[18]
        reg['VL_UNIT_FCP_ST_CONV_ENTRADA'] = linha[19]

    elif registro == "C190":
        reg['CST_ICMS'] = linha[2]
        reg['CFOP'] = linha[3]
        reg['ALIQ_ICMS'] = linha[4]
        reg['VL_OPR'] = linha[5]
        reg['VL_BC_ICMS'] = linha[6]
        reg['VL_ICMS'] = linha[7]
        reg['VL_BC_ICMS_'] = linha[8]
        reg['VL_ICMS_ST'] = linha[9]
        reg['VL_RED_BC'] = linha[10]
        reg['VL_IPI'] = linha[11]
        reg['COD_OBS'] = linha[12]

    elif registro == "D100":
        reg['IND_OPER'] = linha[2]
        reg['IND_EMIT'] = linha[3]
        reg['COD_PART'] = linha[4]
        reg['COD_MOD'] = linha[5]
        reg['COD_SIT'] = linha[6]
        reg['SER'] = linha[7]
        reg['SUB'] = linha[8]
        reg['NUM_DOC'] = linha[9]
        reg['CHV_CTE'] = linha[10]
        reg['DT_DOC'] = linha[11]
        reg['DT_A_P'] = linha[12]
        reg['TP_CTE'] = linha[13]
        reg['CHV_CTE_REF'] = linha[14]
        reg['VL_DOC'] = linha[15]
        reg['VL_DESC'] = linha[16]
        reg['IND_FRT'] = linha[17]
        reg['VL_SERV'] = linha[18]
        reg['VL_BC_ICMS'] = linha[19]
        reg['VL_ICMS'] = linha[20]
        reg['VL_NT'] = linha[21]
        reg['COD_INF'] = linha[22]
        reg['COD_CTA'] = linha[23]
        reg['COD_MUN_ORIG'] = linha[24]
        reg['COD_MUN_DEST'] = linha[25]

    elif registro == "D190":
        reg['CST_ICMS'] = linha[2]
        reg['CFOP'] = linha[3]
        reg['ALIQ_ICMS'] = linha[4]
        reg['VL_OPR'] = linha[5]
        reg['VL_BC_ICMS'] = linha[6]
        reg['VL_ICMS'] = linha[7]
        reg['VL_RED_BC'] = linha[8]
        reg['COD_OBS'] = linha[9]

    elif registro == "E110":
        reg['VL_TOT_DEBITOS'] = linha[2]
        reg['VL_AJ_DEBITOS'] = linha[3]
        reg['VL_TOT_AJ_DEBITOS'] = linha[4]
        reg['VL_ESTORNOS_CRED'] = linha[5]
        reg['VL_TOT_CREDITOS'] = linha[6]
        reg['VL_AJ_CREDITOS'] = linha[7]
        reg['VL_TOT_AJ_CREDITOS'] = linha[8]
        reg['VL_ESTORNOS_DEB'] = linha[9]
        reg['VL_SLD_CREDOR_ANT'] = linha[10]
        reg['VL_SLD_APURADO'] = linha[11]
        reg['VL_TOT_DED'] = linha[12]
        reg['VL_ICMS_RECOLHER'] = linha[13]
        reg['VL_SLD_CREDOR_TRANSPORTAR'] = linha[14]
        reg['DEB_ESP'] = linha[15]

    elif registro == "E115":
        reg['COD_INF_ADIC'] = linha[2]
        reg['VL_INF_ADIC'] = linha[3]
        reg['DESCR_COMPL_AJ'] = linha[4]

    elif registro == "E210":
        reg['IND_MOV_ST'] = linha[2]
        reg['VL_SLD_CRED_ANT_ST'] = linha[3]
        reg['VL_DEVOL_ST'] = linha[4]
        reg['VL_RESSARC_ST'] = linha[5]
        reg['VL_OUT_CRED_ST'] = linha[6]
        reg['VL_AJ_CREDITOS_ST'] = linha[7]
        reg['VL_RETENCAO_ST'] = linha[8]
        reg['VL_OUT_DEB_ST'] = linha[9]
        reg['VL_AJ_DEBITOS_ST'] = linha[10]
        reg['VL_SLD_DEV_ANT_ST'] = linha[11]
        reg['VL_DEDUCOES_ST'] = linha[12]
        reg['VL_ICMS_RECOL_ST'] = linha[13]
        reg['VL_SLD_CRED_ST_TRANSPORTAR'] = linha[14]
        reg['DEB_ESP_ST'] = linha[15]

    elif registro == "H010":
        reg['COD_ITEM'] = linha[2]
        reg['UNID'] = linha[3]
        reg['QTD'] = linha[4]
        reg['VL_UNIT'] = linha[5]
        reg['VL_ITEM'] = linha[6]
        reg['IND_PROP'] = linha[7]
        reg['COD_PART'] = linha[8]
        reg['TXT_COMPL'] = linha[9]
        reg['COD_CTA'] = linha[10]
        reg['VL_ITEM_IR'] = linha[11]

    elif registro == "H030":
        reg['VL_ICMS_OP'] = linha[2]
        reg['VL_BC_ICMS_ST'] = linha[3]
        reg['VL_ICMS_ST'] = linha[4]
        reg['VL_FCP'] = linha[5]

    elif registro == "1250":
        reg['VL_CREDITO_ICMS_OP'] = linha[2]
        reg['VL_ICMS_ST_REST'] = linha[3]
        reg['VL_FCP_ST_REST'] = linha[4]
        reg['VL_ICMS_ST_COMPL'] = linha[5]
        reg['VL_FCP_ST_COMPL'] = linha[6]

    elif registro == "1255":
        reg['COD_MOT_REST_COMPL'] = linha[2]
        reg['VL_CREDITO_ICMS_OP_MOT'] = linha[3]
        reg['VL_ICMS_ST_REST_MOT'] = linha[4]
        reg['VL_FCP_ST_REST_MOT'] = linha[5]
        reg['VL_ICMS_ST_COMPL_MOT'] = linha[6]
        reg['VL_FCP_ST_COMPL_MOT'] = linha[7]

    elif registro == "1601":
        reg['COD_PART_IP'] = linha[2]
        reg['COD_PART_IT'] = linha[3]
        reg['TOT_VS'] = linha[4]
        reg['TOT_ISS'] = linha[5]
        reg['TOT_OUTROS'] = linha[6]


    if registro in ['C180', 'C181']:
        if tipo == TIPO_CSV:
            reg['PRODUTO_PAI'] = produtoPai
            reg['PARTIC_PAI'] = particPai
            reg['ID_PAI'] = idPai
        elif tipo == TIPO_DB:
            reg['PRODUTO_PAI'] = linha[len(reg)]
            reg['PARTIC_PAI'] = linha[len(reg)]
            reg['ID_PAI'] = linha[len(reg)]

    if registro in ['C112', 'C113', 'C170', 'C185', 'C186', 'C190', 'D190']:
        if tipo == TIPO_CSV:
            reg['PARTIC_PAI'] = particPai
            reg['ID_PAI'] = idPai
        elif tipo == TIPO_DB:
            reg['PARTIC_PAI'] = linha[len(reg)]
            reg['ID_PAI'] = linha[len(reg)]

    if registro in  ['0175', '0205', '0220', 'H030']:
        if tipo == TIPO_CSV:
            reg['ID_PAI'] = idPai
        elif tipo == TIPO_DB:
            reg['ID_PAI'] = linha[len(reg)]
    
    if tipo == TIPO_CSV:
        reg['NLINHA'] = nlinha
    elif tipo == TIPO_DB:
        reg['NLINHA'] = linha[len(reg)]

    return reg

            