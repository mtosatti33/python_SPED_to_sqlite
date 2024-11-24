def insert_data(registro, reg):
    if registro == '0000':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'], 
                reg['COD_VER'], 
                reg['COD_FIN'], 
                reg['DT_INI'], 
                reg['DT_FIN'], 
                reg['NOME'], 
                reg['CNPJ'], 
                reg['CPF'], 
                reg['UF'], 
                reg['IE'], 
                reg['COD_MUN'], 
                reg['IM'], 
                reg['SUFRAMA'], 
                reg['IND_PERFIL'], 
                reg['IND_ATIV'],
                reg['NLINHA']
        )
    elif registro == '0100':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['NOME'],
                reg['CPF'],
                reg['CRC'],
                reg['CNPJ'],
                reg['CEP'],
                reg['END'],
                reg['NUM'],
                reg['COMPL'],
                reg['BAIRRO'],
                reg['FONE'],
                reg['FAX'],
                reg['EMAIL'],
                reg['COD_MUN'],
                reg['NLINHA']
            )
    
    elif registro == '0150':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['COD_PART'],
                reg['NOME'],
                reg['COD_PAIS'],
                reg['CNPJ'],
                reg['CPF'],
                reg['IE'],
                reg['COD_MUN'],
                reg['SUFRAMA'],
                reg['END'],
                reg['NUM'],
                reg['COMPL'],
                reg['BAIRRO'],
                reg['NLINHA']
                )
    
    elif registro =='0175':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'], 
                reg['DT_ALT'], 
                reg['NR_CAMPO'], 
                reg['CONT_ANT'], 
                reg['ID_PAI'],
                reg['NLINHA']
                    )
    
    elif registro == '0190':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['UNID'],
                reg['DESCR'],
                reg['NLINHA']
            )
    elif registro == '0200':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['COD_ITEM'],
                reg['DESCR_ITEM'],
                reg['COD_BARRA'],
                reg['COD_ANT_ITEM'],
                reg['UNID_INV'],
                reg['TIPO_ITEM'],
                reg['COD_NCM'],
                reg['EX_IPI'],
                reg['COD_GEN'],
                reg['COD_LST'],
                reg['ALIQ_ICMS'],
                reg['CEST'],
                reg['NLINHA']
            )
    
    elif registro == '0205':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['DESCR_ANT_ITEM'],
                reg['DT_INI'],
                reg['DT_FIM'],
                reg['COD_ANT_ITEM'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == '0220':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['UNID_CONV'],
                reg['FAT_CONV'],
                reg['COD_BARRA'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == '0400':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['COD_NAT'],
                reg['DESCR_NAT'],
                reg['NLINHA']
            )
    
    elif registro == 'C100':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['IND_OPER'],
                reg['IND_EMIT'],
                reg['COD_PART'],
                reg['COD_MOD'],
                reg['COD_SIT'],
                reg['SER'],
                reg['NUM_DOC'],
                reg['CHV_NFE'],
                reg['DT_DOC'],
                reg['DT_E_S'],
                reg['VL_DOC'],
                reg['IND_PGTO'],
                reg['VL_DESC'],
                reg['VL_ABAT_NT'],
                reg['VL_MERC'],
                reg['IND_FRT'],
                reg['VL_FRT'],
                reg['VL_SEG'],
                reg['VL_OUT_DA'],
                reg['VL_BC_ICMS'],
                reg['VL_ICMS'],
                reg['VL_BC_ICMS_ST'],
                reg['VL_ICMS_ST'],
                reg['VL_IPI'],
                reg['VL_PIS'],
                reg['VL_COFINS'],
                reg['VL_PIS_ST'],
                reg['VL_COFINS_ST'],
                reg['NLINHA']
            )
    
    elif registro == 'C112':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['COD_DA'],
                reg['UF'],
                reg['NUM_DA'],
                reg['COD_AUT'],
                reg['VL_DA'],
                reg['DT_VCTO'],
                reg['DT_PGTO'], 
                reg['PARTIC_PAI'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == 'C113':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['IND_OPER'], 
                reg['IND_EMIT'], 
                reg['COD_PART'], 
                reg['COD_MOD'], 
                reg['SER'], 
                reg['SUB'], 
                reg['NUM_DOC'], 
                reg['DT_DOC'], 
                reg['CHV_DOCe'],  
                reg['PARTIC_PAI'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == 'C170':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['NUM_ITEM'], 
                reg['COD_ITEM'], 
                reg['DESCR_COMPL'], 
                reg['QTD'], 
                reg['UNID'], 
                reg['VL_ITEM'], 
                reg['VL_DESC'], 
                reg['IND_MOV'], #10
                reg['CST_ICMS'], 
                reg['CFOP'], 
                reg['COD_NAT'], 
                reg['VL_BC_ICMS'], 
                reg['ALIQ_ICMS'], 
                reg['VL_ICMS'], 
                reg['VL_BC_ICMS_ST'], 
                reg['ALIQ_ST'], 
                reg['VL_ICMS_ST'], 
                reg['IND_APUR'], #20
                reg['CST_IPI'], 
                reg['COD_ENQ'], 
                reg['VL_BC_IPI'], 
                reg['ALIQ_IPI'], 
                reg['VL_IPI'], 
                reg['CST_PIS'], 
                reg['VL_BC_PIS'], 
                reg['ALIQ_PIS_PCT'], 
                reg['QUANT_BC_PIS'], 
                reg['ALIQ_PIS_RS'], #30
                reg['VL_PIS'], 
                reg['CST_COFINS'], 
                reg['VL_BC_COFINS'], 
                reg['ALIQ_COFINS_PCT'], 
                reg['QUANT_BC_COFINS'], 
                reg['ALIQ_COFINS_RS'], 
                reg['VL_COFINS'], 
                reg['COD_CTA'], 
                reg['VL_ABAT_NT'], 
                reg['PARTIC_PAI'], #40
                reg['ID_PAI'],
                reg['NLINHA'] #42
            )
    
    elif registro == 'C180':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['COD_RESP_RET'], 
                reg['QUANT_CONV'], 
                reg['UNID'], 
                reg['VL_UNIT_CONV'], 
                reg['VL_UNIT_ICMS_OP_CONV'], 
                reg['VL_UNIT_BC_ICMS_ST_CONV'], 
                reg['VL_UNIT_ICMS_ST_CONV'], 
                reg['VL_UNIT_FCP_ST_CONV'], 
                reg['COD_DA'], 
                reg['NUM_DA'], 
                reg['PRODUTO_PAI'], 
                reg['PARTIC_PAI'],
                reg['ID_PAI'], 
                reg['NLINHA']
                )
    
    elif registro == 'C181':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['COD_MOT_REST_COMPL'],
                reg['QUANT_CONV'],
                reg['UNID'],
                reg['COD_MOD_SAIDA'],
                reg['SERIE_SAIDA'],
                reg['ECF_FAB_SAIDA'],
                reg['NUM_DOC_SAIDA'],
                reg['CHV_DFE_SAIDA'],
                reg['DT_DOC_SAIDA'],
                reg['NUM_ITEM_SAIDA'],
                reg['VL_UNIT_CONV_SAIDA'],
                reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA'],
                reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA'],
                reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA'],
                reg['VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA'],
                reg['VL_UNIT_ICMS_OP_CONV_SAIDA'],
                reg['VL_UNIT_ICMS_ST_CONV_REST'],
                reg['VL_UNIT_FCP_ST_CONV_REST'],
                reg['VL_UNIT_ICMS_ST_CONV_COMPL'],
                reg['VL_UNIT_FCP_ST_CONV_COMPL'],
                reg['PRODUTO_PAI'], 
                reg['PARTIC_PAI'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == 'C185':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['NUM_ITEM'], 
                reg['COD_ITEM'], 
                reg['CST_ICMS'], 
                reg['CFOP'], 
                reg['COD_MOT_REST_COMPL'], 
                reg['QUANT_CONV'], 
                reg['UNID'], 
                reg['VL_UNIT_CONV'], 
                reg['VL_UNIT_ICMS_NA_OPERACAO_CONV'], 
                reg['VL_UNIT_ICMS_OP_ESTOQUE_CONV'], 
                reg['VL_UNIT_ICMS_ST_ESTOQUE_CONV'], 
                reg['VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV'], 
                reg['VL_UNIT_ICMS_ST_CONV_REST'], 
                reg['VL_UNIT_FCP_ST_CONV_REST'], 
                reg['VL_UNIT_ICMS_ST_CONV_COMPL'], 
                reg['VL_UNIT_FCP_ST_CONV_'],  
                reg['PARTIC_PAI'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == 'C186':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['NUM_ITEM'], 
                reg['COD_ITEM'], 
                reg['CST_ICMS'], 
                reg['CFOP'], 
                reg['COD_MOT_REST_COMPL'], 
                reg['QUANT_CONV'], 
                reg['UNID'], 
                reg['COD_MOD_ENTRADA'], 
                reg['SERIE_ENTRADA'], 
                reg['NUM_DOC_ENTRADA'], 
                reg['CHV_DFE_ENTRADA'], 
                reg['DT_DOC_ENTRADA'], 
                reg['NUM_ITEM_ENTRADA'], 
                reg['VL_UNIT_CONV_ENTRADA'], 
                reg['VL_UNIT_ICMS_OP_CONV_'], 
                reg['VL_UNIT_BC_ICMS_ST'], 
                reg['VL_UNIT_ICMS_ST_CONV_ENTRADA'], 
                reg['VL_UNIT_FCP_ST_CONV_ENTRADA'],  
                reg['PARTIC_PAI'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == 'C190':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['CST_ICMS'], 
                reg['CFOP'], 
                reg['ALIQ_ICMS'], 
                reg['VL_OPR'], 
                reg['VL_BC_ICMS'], 
                reg['VL_ICMS'], 
                reg['VL_BC_ICMS_'], 
                reg['VL_ICMS_ST'], 
                reg['VL_RED_BC'], 
                reg['VL_IPI'], 
                reg['COD_OBS'],  
                reg['PARTIC_PAI'],
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == 'E110':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['VL_TOT_DEBITOS'], 
                reg['VL_AJ_DEBITOS'], 
                reg['VL_TOT_AJ_DEBITOS'], 
                reg['VL_ESTORNOS_CRED'], 
                reg['VL_TOT_CREDITOS'], 
                reg['VL_AJ_CREDITOS'], 
                reg['VL_TOT_AJ_CREDITOS'], 
                reg['VL_ESTORNOS_DEB'], 
                reg['VL_SLD_CREDOR_ANT'], 
                reg['VL_SLD_APURADO'], 
                reg['VL_TOT_DED'], 
                reg['VL_ICMS_RECOLHER'], 
                reg['VL_SLD_CREDOR_TRANSPORTAR'], 
                reg['DEB_ESP'],
                reg['NLINHA']
                )
    
    elif registro == 'E115':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['COD_INF_ADIC'], 
                reg['VL_INF_ADIC'], 
                reg['DESCR_COMPL_AJ'],
                reg['NLINHA']
                )
    
    elif registro == 'E210':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['IND_MOV_ST'], 
                reg['VL_SLD_CRED_ANT_ST'], 
                reg['VL_DEVOL_ST'], 
                reg['VL_RESSARC_ST'], 
                reg['VL_OUT_CRED_ST'], 
                reg['VL_AJ_CREDITOS_ST'], 
                reg['VL_RETENCAO_ST'], 
                reg['VL_OUT_DEB_ST'], 
                reg['VL_AJ_DEBITOS_ST'], 
                reg['VL_SLD_DEV_ANT_ST'], 
                reg['VL_DEDUCOES_ST'], 
                reg['VL_ICMS_RECOL_ST'], 
                reg['VL_SLD_CRED_ST_TRANSPORTAR'], 
                reg['DEB_ESP_ST'],
                reg['NLINHA']
                )
    
    elif registro == 'H010':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['COD_ITEM'], 
                reg['UNID'], 
                reg['QTD'], 
                reg['VL_UNIT'], 
                reg['VL_ITEM'], 
                reg['IND_PROP'], 
                reg['COD_PART'], 
                reg['TXT_COMPL'], 
                reg['COD_CTA'], 
                reg['VL_ITEM_IR'],
                reg['NLINHA']
                )
    
    elif registro == 'H030':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'], 
                reg['REG'], 
                reg['VL_ICMS_OP'], 
                reg['VL_BC_ICMS_ST'], 
                reg['VL_ICMS_ST'], 
                reg['VL_FCP'], 
                reg['ID_PAI'],
                reg['NLINHA']
                )
    
    elif registro == '1250':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['VL_CREDITO_ICMS_OP'],
                reg['VL_ICMS_ST_REST'],
                reg['VL_FCP_ST_REST'],
                reg['VL_ICMS_ST_COMPL'],
                reg['VL_FCP_ST_COMPL'],
                reg['NLINHA']
                )
    
    elif registro == '1255':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['COD_MOT_REST_COMPL'],
                reg['VL_CREDITO_ICMS_OP_MOT'],
                reg['VL_ICMS_ST_REST_MOT'],
                reg['VL_FCP_ST_REST_MOT'],
                reg['VL_ICMS_ST_COMPL_MOT'],
                reg['VL_FCP_ST_COMPL_MOT'],
                reg['NLINHA']
                )
    
    elif registro == '1601':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['COD_PART_IP'],
                reg['COD_PART_IT'],
                reg['TOT_VS'],
                reg['TOT_ISS'],
                reg['TOT_OUTROS'],
                reg['NLINHA']
                )
    
    elif registro == 'D100':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['IND_OPER'],
                reg['IND_EMIT'],
                reg['COD_PART'],
                reg['COD_MOD'],
                reg['COD_SIT'],
                reg['SER'],
                reg['SUB'],
                reg['NUM_DOC'],
                reg['CHV_CTE'],
                reg['DT_DOC'],
                reg['DT_A_P'],
                reg['TP_CTE'],
                reg['CHV_CTE_REF'],
                reg['VL_DOC'],
                reg['VL_DESC'],
                reg['IND_FRT'],
                reg['VL_SERV'],
                reg['VL_BC_ICMS'],
                reg['VL_ICMS'],
                reg['VL_NT'],
                reg['COD_INF'],
                reg['COD_CTA'],
                reg['COD_MUN_ORIG'],
                reg['COD_MUN_DEST'],
                reg['NLINHA']
                )

    elif registro == 'D190':
        return "insert into Reg{} values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
                registro,
                reg['ID'],
                reg['REG'],
                reg['CST_ICMS'],
                reg['CFOP'],
                reg['ALIQ_ICMS'],
                reg['VL_OPR'],
                reg['VL_BC_ICMS'],
                reg['VL_ICMS'],
                reg['VL_RED_BC'],
                reg['COD_OBS'], 
                reg['PARTIC_PAI'],
                reg['ID_PAI'],
                reg['NLINHA']
                )