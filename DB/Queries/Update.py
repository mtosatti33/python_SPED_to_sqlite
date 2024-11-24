def update_data(registro):
    if registro == "0200":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'ALIQ_ICMS', 'ALIQ_ICMS'
            )
    
    if registro == "0220":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'FAT_CONV', 'FAT_CONV'
            )
    
    if registro == "C100":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_DOC','VL_DOC',
            'VL_DESC','VL_DESC',
            'VL_ABAT_NT', 'VL_ABAT_NT',
            'VL_MERC', 'VL_MERC',
            'VL_FRT', 'VL_FRT',
            'VL_SEG', 'VL_SEG',
            'VL_OUT_DA', 'VL_OUT_DA',
            'VL_BC_ICMS', 'VL_BC_ICMS',
            'VL_ICMS', 'VL_ICMS',
            'VL_BC_ICMS_ST', 'VL_BC_ICMS_ST',
            'VL_ICMS_ST', 'VL_ICMS_ST',
            'VL_IPI', 'VL_IPI',
            'VL_PIS', 'VL_PIS',
            'VL_COFINS', 'VL_COFINS',
            'VL_PIS_ST', 'VL_PIS_ST', 
            'VL_COFINS_ST', 'VL_COFINS_ST'
            )
    
    if registro == "C112":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_DA', 'VL_DA'
            )
    
    if registro == "C170":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_ITEM', 'VL_ITEM', 
            'VL_DESC', 'VL_DESC', 
            'VL_BC_ICMS', 'VL_BC_ICMS', 
            'ALIQ_ICMS', 'ALIQ_ICMS', 
            'VL_ICMS', 'VL_ICMS', 
            'VL_BC_ICMS_ST', 'VL_BC_ICMS_ST', 
            'ALIQ_ST', 'ALIQ_ST', 
            'VL_ICMS_ST', 'VL_ICMS_ST', 
            'VL_BC_IPI', 'VL_BC_IPI', 
            'ALIQ_IPI', 'ALIQ_IPI', 
            'VL_IPI', 'VL_IPI', 
            'CST_PIS', 'CST_PIS', 
            'VL_BC_PIS', 'VL_BC_PIS', 
            'ALIQ_PIS_PCT', 'ALIQ_PIS_PCT', 
            'QUANT_BC_PIS', 'QUANT_BC_PIS', 
            'ALIQ_PIS_RS', 'ALIQ_PIS_RS', 
            'VL_PIS', 'VL_PIS', 
            'CST_COFINS', 'CST_COFINS', 
            'VL_BC_COFINS', 'VL_BC_COFINS', 
            'ALIQ_COFINS_PCT', 'ALIQ_COFINS_PCT', 
            'QUANT_BC_COFINS', 'QUANT_BC_COFINS', 
            'ALIQ_COFINS_RS', 'ALIQ_COFINS_RS', 
            'VL_COFINS', 'VL_COFINS', 
            'COD_CTA', 'COD_CTA', 
            'VL_ABAT_NT', 'VL_ABAT_NT'
            )
    
    if registro == "C180":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'QUANT_CONV', 'QUANT_CONV', 
            'VL_UNIT_CONV', 'VL_UNIT_CONV', 
            'VL_UNIT_ICMS_OP_CONV', 'VL_UNIT_ICMS_OP_CONV', 
            'VL_UNIT_BC_ICMS_ST_CONV', 'VL_UNIT_BC_ICMS_ST_CONV', 
            'VL_UNIT_ICMS_ST_CONV', 'VL_UNIT_ICMS_ST_CONV', 
            'VL_UNIT_FCP_ST_CONV', 'VL_UNIT_FCP_ST_CONV'
            )
    
    if registro == "C181":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'QUANT_CONV',   'QUANT_CONV', 
            'VL_UNIT_CONV_SAIDA', 'VL_UNIT_CONV_SAIDA', 
            'VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV_SAIDA', 
            'VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV_SAIDA', 
            'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV_SAIDA', 
            'VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA', 'VL_UNIT_ICMS_NA_OPERACAO_CONV_SAIDA', 
            'VL_UNIT_ICMS_OP_CONV_SAIDA', 'VL_UNIT_ICMS_OP_CONV_SAIDA', 
            'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_REST', 
            'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 
            'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_ICMS_ST_CONV_COMPL', 
            'VL_UNIT_FCP_ST_CONV_COMPL', 'VL_UNIT_FCP_ST_CONV_COMPL'
            )
    
    if registro == "C185":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'QUANT_CONV', 'QUANT_CONV', 
            'VL_UNIT_CONV', 'VL_UNIT_CONV', 
            'VL_UNIT_ICMS_NA_OPERACAO_CONV', 'VL_UNIT_ICMS_NA_OPERACAO_CONV', 
            'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 'VL_UNIT_ICMS_OP_ESTOQUE_CONV', 
            'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_ICMS_ST_ESTOQUE_CONV', 
            'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 'VL_UNIT_FCP_ICMS_ST_ESTOQUE_CONV', 
            'VL_UNIT_ICMS_ST_CONV_REST', 'VL_UNIT_ICMS_ST_CONV_REST', 
            'VL_UNIT_FCP_ST_CONV_REST', 'VL_UNIT_FCP_ST_CONV_REST', 
            'VL_UNIT_ICMS_ST_CONV_COMPL', 'VL_UNIT_ICMS_ST_CONV_COMPL', 
            'VL_UNIT_FCP_ST_CONV_', 'VL_UNIT_FCP_ST_CONV_'
            )
    
    if registro == "C186":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'QUANT_CONV', 'QUANT_CONV', 
            'VL_UNIT_CONV_ENTRADA', 'VL_UNIT_CONV_ENTRADA', 
            'VL_UNIT_ICMS_OP_CONV_', 'VL_UNIT_ICMS_OP_CONV_', 
            'VL_UNIT_BC_ICMS_ST', 'VL_UNIT_BC_ICMS_ST', 
            'VL_UNIT_ICMS_ST_CONV_ENTRADA', 'VL_UNIT_ICMS_ST_CONV_ENTRADA', 
            'VL_UNIT_FCP_ST_CONV_ENTRADA', 'VL_UNIT_FCP_ST_CONV_ENTRADA'
            )
    
    if registro == "C190":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'ALIQ_ICMS', 'ALIQ_ICMS', 
            'VL_OPR', 'VL_OPR', 
            'VL_BC_ICMS', 'VL_BC_ICMS', 
            'VL_ICMS', 'VL_ICMS', 
            'VL_BC_ICMS_', 'VL_BC_ICMS_', 
            'VL_ICMS_ST', 'VL_ICMS_ST', 
            'VL_RED_BC', 'VL_RED_BC', 
            'VL_IPI', 'VL_IPI'
            )
    
    if registro == "D100":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_DOC', 'VL_DOC',
            'VL_DESC', 'VL_DESC',
            'VL_SERV', 'VL_SERV',
            'VL_BC_ICMS', 'VL_BC_ICMS',
            'VL_ICMS', 'VL_ICMS',
            'VL_NT', 'VL_NT'
            )
    
    if registro == "D190":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'ALIQ_ICMS', 'ALIQ_ICMS',
            'VL_OPR', 'VL_OPR',
            'VL_BC_ICMS', 'VL_BC_ICMS',
            'VL_ICMS', 'VL_ICMS',
            'VL_RED_BC', 'VL_RED_BC',
            'ID_PAI', 'ID_PAI'
            )
    
    if registro == "E110":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_TOT_DEBITOS', 'VL_TOT_DEBITOS',
            'VL_AJ_DEBITOS', 'VL_AJ_DEBITOS',
            'VL_TOT_AJ_DEBITOS', 'VL_TOT_AJ_DEBITOS',
            'VL_ESTORNOS_CRED', 'VL_ESTORNOS_CRED',
            'VL_TOT_CREDITOS', 'VL_TOT_CREDITOS',
            'VL_AJ_CREDITOS', 'VL_AJ_CREDITOS',
            'VL_TOT_AJ_CREDITOS', 'VL_TOT_AJ_CREDITOS',
            'VL_ESTORNOS_DEB', 'VL_ESTORNOS_DEB',
            'VL_SLD_CREDOR_ANT', 'VL_SLD_CREDOR_ANT',
            'VL_SLD_APURADO', 'VL_SLD_APURADO',
            'VL_TOT_DED', 'VL_TOT_DED',
            'VL_ICMS_RECOLHER', 'VL_ICMS_RECOLHER',
            'VL_SLD_CREDOR_TRANSPORTAR', 'VL_SLD_CREDOR_TRANSPORTAR',
            'DEB_ESP', 'DEB_ESP'
            )
    
    if registro == "E115":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_INF_ADIC', 'VL_INF_ADIC'
            )
    
    if registro == "E210":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_SLD_CRED_ANT_ST', 'VL_SLD_CRED_ANT_ST',
            'VL_DEVOL_ST', 'VL_DEVOL_ST',
            'VL_RESSARC_ST', 'VL_RESSARC_ST',
            'VL_OUT_CRED_ST', 'VL_OUT_CRED_ST',
            'VL_AJ_CREDITOS_ST', 'VL_AJ_CREDITOS_ST',
            'VL_RETENCAO_ST', 'VL_RETENCAO_ST',
            'VL_OUT_DEB_ST', 'VL_OUT_DEB_ST',
            'VL_AJ_DEBITOS_ST', 'VL_AJ_DEBITOS_ST',
            'VL_SLD_DEV_ANT_ST', 'VL_SLD_DEV_ANT_ST',
            'VL_DEDUCOES_ST', 'VL_DEDUCOES_ST',
            'VL_ICMS_RECOL_ST', 'VL_ICMS_RECOL_ST',
            'VL_SLD_CRED_ST_TRANSPORTAR', 'VL_SLD_CRED_ST_TRANSPORTAR',
            'DEB_ESP_ST', 'DEB_ESP_ST'
            )
    
    if registro == "H010":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'QTD', 'QTD', 
            'VL_UNIT', 'VL_UNIT', 
            'VL_ITEM', 'VL_ITEM', 
            'VL_ITEM_IR', 'VL_ITEM_IR'
            )
    
    if registro == "H030":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_ICMS_OP', 'VL_ICMS_OP', 
            'VL_BC_ICMS_ST', 'VL_BC_ICMS_ST', 
            'VL_ICMS_ST', 'VL_ICMS_ST', 
            'VL_FCP', 'VL_FCP'
            )
    
    if registro == "1250":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_CREDITO_ICMS_OP', 'VL_CREDITO_ICMS_OP',
            'VL_ICMS_ST_REST', 'VL_ICMS_ST_REST',
            'VL_FCP_ST_REST', 'VL_FCP_ST_REST',
            'VL_ICMS_ST_COMPL', 'VL_ICMS_ST_COMPL',
            'VL_FCP_ST_COMPL', 'VL_FCP_ST_COMPL'
            )
    
    if registro == "1255":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'VL_CREDITO_ICMS_OP_MOT', 'VL_CREDITO_ICMS_OP_MOT',
            'VL_ICMS_ST_REST_MOT', 'VL_ICMS_ST_REST_MOT',
            'VL_FCP_ST_REST_MOT', 'VL_FCP_ST_REST_MOT',
            'VL_ICMS_ST_COMPL_MOT', 'VL_ICMS_ST_COMPL_MOT',
            'VL_FCP_ST_COMPL_MOT', 'VL_FCP_ST_COMPL_MOT'
            )
    
    if registro == "1601":
        return '''update Reg{} set 
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.'),
        {} = REPLACE({}, ',', '.');
        '''.format(
            registro,
            'TOT_VS', 'TOT_VS',
            'TOT_ISS', 'TOT_ISS',
            'TOT_OUTROS', 'TOT_OUTROS'
            )