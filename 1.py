import json

def sacar_Ratios(JSON_ARCHIVO):

    # TOTALES
    ACTIVO_CORRIENTE = 0
    ACTIVO_NO_CORRIENTE = 0
    PASIVO_NO_CORRIENTE = 0
    PASIVO_CORRIENTE = 0
    PATRIMONIO_NETO = 0
    # AC
    CAJA_Y_BANCOS_CORRIENTE = 0
    INVERSIONES_CORRIENTE = 0
    CREDITOS_POR_VENTAS_CORRIENTE = 0
    CREDITOS_FISCALES_CORRIENTE = 0
    OTROS_CREDITOS_CORRIENTE = 0
    BIENES_DE_CAMBIO_CORRIENTE = 0
    ACCIONISTAS_SOCIOS_CORRIENTE = 0
    OTROS_CORRIENTE = 0
    #ANC 
    CREDITOS_FISCALES_N = 0
    ACCIONISTAS_SOCIOS_N = 0
    INVERSIONES_N = 0
    OTROS_N = 0
    BIENES_DE_USO_N = 0
    # PC
    DEUDAS_COMERCIALES_P_CORRIENTE = 0 
    ANTICIPO_DE_CLIENTES_P_CORRIENTE = 0 
    DEUDAS_BANCARIAS_FINANCIERAS_P_CORRIENTE = 0
    DEUDAS_SOCIALES_Y_FISCALES_P_CORRIENTE = 0
    MORATORIAS_IMPOSITIVAS_P_CORRIENTE = 0
    ACCIONISTAS_SOCIOS_P_CORRIENTE = 0
    PASIVO_CONCURSAL_P_CORRIENTE = 0
    OTRAS_DEUDAS_P_CORRIENTE = 0
    # PNC
    DEUDAS_COMERCIALES_P_NC = 0 
    ANTICIPO_DE_CLIENTES_P_NC = 0 
    DEUDAS_BANCARIAS_FINANCIERAS_P_NC = 0
    DEUDAS_SOCIALES_Y_FISCALES_P_NC = 0
    MORATORIAS_IMPOSITIVAS_P_NC = 0
    ACCIONISTAS_SOCIOS_P_NC = 0
    PASIVO_CONCURSAL_P_NC = 0
    OTRAS_DEUDAS_P_NC = 0
    # ER

    COSTO_DE_VENTAS_ER = 0
    GASTOS_COMERCIALES_ER = 0
    GASTOS_ADMINISTRATIVOS_ER = 0
    OTROS_GASTOS_ER = 0
    RESULTADOS_FINANCIEROS_Y_POR_TENENCIA_ER = 0
    RECPAM_ER = 0
    OTROS_INGRESOS_ER = 0
    OTROS_EGRESOS_ER = 0
    IMPUESTO_A_LAS_GANANCIAS_ER = 0

    RESULTADO_OPERATIVO_ER = 0
    VENTAS_TOTALES_ER = 0
    RESULTADO_NETO_ER = 0

    with open(JSON_ARCHIVO) as contenido:

        res = json.load(contenido)
        ESP = res["ESP"]
        ER = res["ER"]

        for i in ESP :

            # TOTALES
            if i["groupClass"]["class"] == "TOTAL ACTIVO CORRIENTE":
                    ACTIVO_CORRIENTE += float(i.get("order_1",0).get("value",0))
            if i["groupClass"]["class"] == "TOTAL ACTIVO NO CORRIENTE":
                    ACTIVO_NO_CORRIENTE += float(i.get("order_1",0).get("value",0))
            if i["groupClass"]["class"] == "TOTAL PASIVO NO CORRIENTE":
                    PASIVO_NO_CORRIENTE += float(i.get("order_1",0).get("value",0))
            if i["groupClass"]["class"] == "TOTAL PASIVO CORRIENTE":
                    PASIVO_CORRIENTE += float(i.get("order_1",0).get("value",0))
            if i["groupClass"]["class"] == "TOTAL PATRIMONIO NETO":
                    PATRIMONIO_NETO += float(i.get("order_1",0).get("value",0))

            # AC
            if i["groupClass"]["group"] == "ACTIVO CORRIENTE":
                if i["groupClass"]["class"] == "CAJA Y BANCOS":
                    CAJA_Y_BANCOS_CORRIENTE = CAJA_Y_BANCOS_CORRIENTE + float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "INVERSIONES":
                    INVERSIONES_CORRIENTE = INVERSIONES_CORRIENTE + float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "CREDITOS POR VENTAS":
                    CREDITOS_POR_VENTAS_CORRIENTE = CREDITOS_POR_VENTAS_CORRIENTE + float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "CREDITOS FISCALES": 
                    CREDITOS_FISCALES_CORRIENTE = CREDITOS_FISCALES_CORRIENTE + float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "OTROS CREDITOS":
                    OTROS_CREDITOS_CORRIENTE = OTROS_CREDITOS_CORRIENTE + float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "BIENES DE CAMBIO":
                    BIENES_DE_CAMBIO_CORRIENTE = BIENES_DE_CAMBIO_CORRIENTE + float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "ACCIONISTAS / SOCIOS":
                    ACCIONISTAS_SOCIOS_CORRIENTE = ACCIONISTAS_SOCIOS_CORRIENTE + float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "OTROS":
                    OTROS_CORRIENTE = OTROS_CORRIENTE + float(i.get("order_1",0).get("value",0))
            # ANC
            if i["groupClass"]["group"] == "ACTIVO NO CORRIENTE":
                if i["groupClass"]["class"] == "CREDITOS FISCALES":
                    CREDITOS_FISCALES_N += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "ACCIONISTAS / SOCIOS":
                    ACCIONISTAS_SOCIOS_N += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "OTROS":
                    OTROS_N += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "INVERSIONES":
                    INVERSIONES_N += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "BIENES DE USO":
                    BIENES_DE_USO_N += float(i.get("order_1",0).get("value",0))
            # PC
            if i["groupClass"]["group"] == "PASIVO CORRIENTE":
                if i["groupClass"]["class"] == "DEUDAS COMERCIALES":
                    DEUDAS_COMERCIALES_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "ANTICIPO DE CLIENTES":
                    ANTICIPO_DE_CLIENTES_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "DEUDAS BANCARIAS / FINANCIERAS":
                    DEUDAS_BANCARIAS_FINANCIERAS_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "DEUDAS SOCIALES Y FISCALES": 
                    DEUDAS_SOCIALES_Y_FISCALES_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "MORATORIAS IMPOSITIVAS":
                    MORATORIAS_IMPOSITIVAS_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "ACCIONISTAS / SOCIOS":
                    ACCIONISTAS_SOCIOS_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "PASIVO CONCURSAL":
                    PASIVO_CONCURSAL_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "OTRAS DEUDAS":
                    OTRAS_DEUDAS_P_CORRIENTE += float(i.get("order_1",0).get("value",0))
            # PNC   
            if i["groupClass"]["group"] == "PASIVO NO CORRIENTE":
                if i["groupClass"]["class"] == "DEUDAS COMERCIALES":
                    DEUDAS_COMERCIALES_P_NC += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "ANTICIPO DE CLIENTES":
                    ANTICIPO_DE_CLIENTES_P_NC += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "DEUDAS BANCARIAS / FINANCIERAS":
                    DEUDAS_BANCARIAS_FINANCIERAS_P_NC += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "DEUDAS SOCIALES Y FISCALES": 
                    DEUDAS_SOCIALES_Y_FISCALES_P_NC += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "MORATORIAS IMPOSITIVAS":
                    MORATORIAS_IMPOSITIVAS_P_NC += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "ACCIONISTAS / SOCIOS":
                    ACCIONISTAS_SOCIOS_P_NC += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "PASIVO CONCURSAL":
                    PASIVO_CONCURSAL_P_NC += float(i.get("order_1",0).get("value",0))
                if i["groupClass"]["class"] == "OTRAS DEUDAS":
                    OTRAS_DEUDAS_P_NC += float(i.get("order_1",0).get("value",0))

        for i in ER:
            # ESTADO DE RESULTADO TOTALES CALCULADOS
            if i["class"] == "VENTAS TOTALES":
                VENTAS_TOTALES_ER += float(i.get("order_1",0))
            if i["class"] == "RESULTADO OPERATIVO":
                RESULTADO_OPERATIVO_ER += float(i.get("order_1",0))
            if i["class"] == "RESULTADO NETO":
                RESULTADO_NETO_ER += float(i.get("order_1",0))

            # ER OTROS CAMPOS.
            if i["class"] == "COSTO DE VENTAS":
                COSTO_DE_VENTAS_ER += float(i.get("order_1",0))
            if i["class"] == "GASTOS COMERCIALES":
                GASTOS_COMERCIALES_ER += float(i.get("order_1",0))
            if i["class"] == "GASTOS ADMINISTRATIVOS":
                GASTOS_ADMINISTRATIVOS_ER += float(i.get("order_1",0))
            if i["class"] == "OTROS GASTOS":
                OTROS_GASTOS_ER += float(i.get("order_1",0))
            if i["class"] == "RESULTADOS FINANCIEROS Y POR TENENCIA":
                RESULTADOS_FINANCIEROS_Y_POR_TENENCIA_ER += float(i.get("order_1",0))
            if i["class"] == "RECPAM":
                RECPAM_ER += float(i.get("order_1",0))
            if i["class"] == "OTROS INGRESOS":
                OTROS_INGRESOS_ER += float(i.get("order_1",0))
            if i["class"] == "OTROS EGRESOS":
                OTROS_EGRESOS_ER += float(i.get("order_1",0))
            if i["class"] == "IMPUESTO A LAS GANANCIAS":
                IMPUESTO_A_LAS_GANANCIAS_ER += float(i.get("order_1",0))

        liquidez = (ACTIVO_CORRIENTE + ACTIVO_NO_CORRIENTE)/(PASIVO_CORRIENTE + PASIVO_NO_CORRIENTE)
        liquidezCorriente = (ACTIVO_CORRIENTE/PASIVO_CORRIENTE)
        pruebaAcida = (ACTIVO_CORRIENTE-BIENES_DE_CAMBIO_CORRIENTE)/PASIVO_CORRIENTE
        endeudamiento = (PASIVO_NO_CORRIENTE+PASIVO_CORRIENTE)/ PATRIMONIO_NETO
        resultadoNeto = RESULTADO_NETO_ER/VENTAS_TOTALES_ER
        ebitda = RESULTADO_OPERATIVO_ER/VENTAS_TOTALES_ER
        cteo = (CAJA_Y_BANCOS_CORRIENTE+BIENES_DE_CAMBIO_CORRIENTE+CREDITOS_POR_VENTAS_CORRIENTE) / (DEUDAS_BANCARIAS_FINANCIERAS_P_CORRIENTE+DEUDAS_COMERCIALES_P_CORRIENTE)
        roe = RESULTADO_NETO_ER/(PATRIMONIO_NETO)
        roa = RESULTADO_OPERATIVO_ER/(ACTIVO_CORRIENTE+ACTIVO_NO_CORRIENTE) # DBERIA SER MAYOR AL % DE FINANCIACIÓN DE LOS BANCOS
        bsDuso = BIENES_DE_USO_N/(ACTIVO_CORRIENTE+ACTIVO_NO_CORRIENTE)
        coberturaServDeuda = RESULTADO_OPERATIVO_ER/(RESULTADOS_FINANCIEROS_Y_POR_TENENCIA_ER+RECPAM_ER)
        coberturaEfectiva = RESULTADO_OPERATIVO_ER/(RESULTADOS_FINANCIEROS_Y_POR_TENENCIA_ER+DEUDAS_BANCARIAS_FINANCIERAS_P_CORRIENTE)
        rotacion = (360/(VENTAS_TOTALES_ER/CREDITOS_POR_VENTAS_CORRIENTE)) - (360/(COSTO_DE_VENTAS_ER/DEUDAS_COMERCIALES_P_CORRIENTE))
        deudafinpc = DEUDAS_BANCARIAS_FINANCIERAS_P_CORRIENTE/(PASIVO_CORRIENTE+PASIVO_NO_CORRIENTE)
        #Indice de generacion : total pasivo / resultado del ejercicio.    

        print(liquidez)
        print(liquidezCorriente)
        print(pruebaAcida)
        print(endeudamiento)
        print(resultadoNeto)
        print(ebitda)
        print(cteo)
        print(roe)
        print(roa)
        print(bsDuso)
        print(coberturaServDeuda)
        print(coberturaEfectiva)
        print(rotacion)
        print(deudafinpc)

sacar_Ratios("1.json")

# COSTO DE VENTAS
# GASTOS COMERCIALES
# GASTOS ADMINISTRATIVOS
# OTROS GASTOS
# RESULTADOS FINANCIEROS Y POR TENENCIA
# RECPAM
# OTROS INGRESOS
# OTROS EGRESOS
# IMPUESTO A LAS GANANCIAS





# ["groupClass"]["class"]  ---> Aca esta la clase correcta
# order 1 es el más nuevo : ["order_1"]["value"]


# ACTIVO CORREIENTE   ############################# 
# CAJA Y BANCOS
# INVERSIONES
# CREDITOS POR VENTAS
# CREDITOS FISCALES
# OTROS CREDITOS
# BIENES DE CAMBIO
# ACCIONISTAS / SOCIOS
# OTROS

# ACTICO NO CORRIENTE ############################
# INVERSIONES
# BIENES DE USO
# CREDITOS FISCALES
# ACCIONISTAS / SOCIOS
# OTROS

# PASIVO CORRIENTE  ##############################
# DEUDAS COMERCIALES
# ANTICIPO DE CLIENTES
# DEUDAS BANCARIAS / FINANCIERAS
# DEUDAS SOCIALES Y FISCALES
# MORATORIAS IMPOSITIVAS
# ACCIONISTAS / SOCIOS
# PASIVO CONCURSAL
# OTRAS DEUDAS

# PASIVO NO CORRIENTE ###########################
# DEUDAS COMERCIALES
# ANTICIPO DE CLIENTES
# DEUDAS BANCARIAS / FINANCIERAS
# DEUDAS SOCIALES Y FISCALES
# MORATORIAS IMPOSITIVAS
# ACCIONISTAS / SOCIOS
# PASIVO CONCURSAL
# OTRAS DEUDAS


# TOTAL PATRIMONIO NETO
# TOTAL ACTIVO CORRIENTE
# TOTAL ACTIVO NO CORRIENTE
# TOTAL PASIVO CORRIENTE
# TOTAL PASIVO NO CORRIENTE




################################## ESTADO DE RESULTADOS ##############################################
# ["class"]  ---> Aca esta la clase correcta
# ["order_1"]

# VENTAS - MERCADO INTERNO
# VENTAS - MERCADO EXTERNO
# OTRAS VENTAS
# COSTO DE VENTAS
# GASTOS COMERCIALES
# GASTOS ADMINISTRATIVOS
# OTROS GASTOS
# RESULTADOS FINANCIEROS Y POR TENENCIA
# RECPAM
# OTROS INGRESOS
# OTROS EGRESOS
# IMPUESTO A LAS GANANCIAS

# RESULTADO OPERATIVO
# VENTAS TOTALES
# RESULTADO NETO 