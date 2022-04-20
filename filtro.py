# -*- coding: utf-8 -*-
import re,requests,cv2
tt =  ('\U0001F321') # temperatura
rr =  ('\U000026A1') #raio
ss = ('\U0001F6A8') #sirene
gg = ('\U0001F9CA') # gelo
oo = ('\U00002699') # operação
vv = ('\U0001F32A') # ventilador
cc = ('\U0001F39B') # compressor
ii = ('\U0001F9EF') # incendio
ok = ('\U00002705') # ok
nok = ('\U00002B55') # nok
tv = ('\U0001F4FA')
feliz = ('\U0001F642') #feliz






def zabbix_filtro(text1):
    from zabbix_api import ZabbixAPI
    URL = 'http:xxxxxxxxxxx'
    USERNAME = 'USUARIO xxx'
    PASSWORD = 'xxxxxxxxxx'
    try:
        zapi = ZabbixAPI(URL, TimeouT=180)
        zapi.login(USERNAME, PASSWORD)
        print(f'conectado na API do zabbix {zapi.api_version()}')
    except Exception as err:
            print(f'falha ao conectar no servidor do Zabbix\n {err}')

    # o resultado de items sao dicionarios soltos com resultados de output
    items = zapi.item.get({
        'output':['name','lastvalue','description'],
        'hostids': 10519
    })
    listacanal = list()
    listanumero = list()
    for y in items:
        canal = (y['name'])
        canal2 = canal[0:3]
        listanumero.append(canal2)
    if text1 in listanumero:
        listacanal = list()
        for item in items:
            listacanal.append(item)   # colocando listas soltas dentro de uma lista

        for item in listacanal:
            if text1 in item['name']:
                    # print(item['name'])
                    # print(item['description'])
                    # print(item['lastvalue'])
                if item['lastvalue'] == '1':
                    item['lastvalue'] = 'OK'
                else:
                    item['lastvalue'] = 'NOK - ligue'
                result = (f'{item["name"]} está {item["lastvalue"]} no HEADEND! em instantes estarei te enviando INBOX informações desse canal que se encontra no TRANSPORTE {item["description"]}')



                print(result)
                print(len(result))
                return result
    else:
        result = ('Este canal não existe na grade de programação da CLARO! em caso de duvidas digite /ajuda')
        print(result)
        print(len(result))		
        return result

    


# zabbix_filtro('521')

def decoder_filtro(variavel_juntandocaixa):
    decoder = ['DCI10','DCI106','DCI713','DCI738','DCI804',
              'DCR2231','DCR3101','DCR7121','DMC7000','DXC5000',
              'GPON','HDC74X1','HDC74X2','HHDC2','HNB100','HNB200',
              'SAG4KC362','SAG4KC363','THDC4']

    if variavel_juntandocaixa in decoder:
        print('TEM A CAIXA')
        name_caixa = (variavel_juntandocaixa)
        # print(name_caixa)
        # print(len(name_caixa))
        # print(name_caixa)
        return name_caixa
    else:
        name_caixa = ('Este modelo de caixa não existe na operação da CLARO! em caso de duvidas digite /ajuda')
        return name_caixa

# decoder_filtro('GPON')

def now_filtro(variavel_juntandonow):
    now = ['UPDATEID','FREQUÊNCIAS']

    if variavel_juntandonow in now:
        # print('TEM A OPCAO')
        now_juntnado = (variavel_juntandonow)
        # print(name_caixa)
        # print(len(name_caixa))
        # print(name_caixa)
        return now_juntnado
    else:
        print('nao tem essa opcao')
        now_juntnado = ('Opçâo invalida! em caso de duvidas digite /ajuda')
        return now_juntnado

# now_filtro('FREQUENCIAS')


def eletrica_filtro(gerador_cidade):
    from zabbix_api import ZabbixAPI
    URL = 'http://xxxxxxxxx'
    USERNAME = 'USUARIO xxxxx'
    PASSWORD = 'xxxxxxxxxx'
    try:
        zapi = ZabbixAPI(URL, TimeouT=180)
        zapi.login(USERNAME, PASSWORD)
        print(f'conectado na API do zabbix {zapi.api_version()}')
    except Exception as err:
            print(f'falha ao conectar no servidor do Zabbix\n {err}')

    # o resultado de items sao dicionarios soltos com resultados de output
    lista = [{'SVE' : 10372,'PGE' : 10371,'GJA' : 10370,'BTG' : 10524,'STS' : 10530,}]
    for x in lista:
        if gerador_cidade in x:
            identificador = (x[gerador_cidade])
            print(identificador)


    if identificador == 10372:
        items = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': identificador
        })

        ### AR CONDICIONADO ###
        arsv = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': 10546
        })

        B = '   ***CONCESSIONARIA***'
        C = '                   ***GERADOR***'
        D = '                   ***OPERACÃO***'
        E = '                   ** AR COND **'

        valor_final1 =  (
          'SV   'f'   {B}\n\
          {rr}{items[11]["name"]} = {items[11]["lastvalue"]}v\n\
          {rr}{items[12]["name"]} = {items[12]["lastvalue"]}v\n\
          {rr}{items[13]["name"]} = {items[13]["lastvalue"]}v\n\
          {rr}{items[3]["name"]} = {items[3]["lastvalue"]}v\n\
          {rr}{items[4]["name"]} = {items[4]["lastvalue"]}v\n\
          {rr}{items[5]["name"]} = {items[5]["lastvalue"]}v\n\
                 \n{C}\n\
          {ss}{items[8]["name"]} = {items[8]["lastvalue"]}v\n\
          {ss}{items[9]["name"]} = {items[9]["lastvalue"]}v\n\
          {ss}{items[10]["name"]} = {items[10]["lastvalue"]}v\n\
          {ss}{items[0]["name"]} = {items[0]["lastvalue"]}v\n\
          {ss}{items[1]["name"]} = {items[1]["lastvalue"]}v\n\
          {ss}{items[2]["name"]} = {items[2]["lastvalue"]}v\n\
                 \n{D}\n\
          {oo}{items[6]["name"]} = {items[6]["lastvalue"]}v\n\
          {oo}{items[7]["name"]} = {items[7]["lastvalue"]}°C\n\
                      \n{E}\n\
          {gg}{arsv[13]["name"]} = {arsv[13]["lastvalue"]}°C\n\
          {gg}{arsv[14]["name"]} = {arsv[14]["lastvalue"]}°C\n\
          {gg}{arsv[15]["name"]} = {arsv[15]["lastvalue"]}°C       ')


        zapi.logout()
        return valor_final1

    if identificador == 10371:
        items = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': identificador
        })

        ### AR CONDICIONADO ###
        arpg = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': 10528
        })

        arpg1 = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': 10379
        })

        # print(items)
        print(f'{items[0]["name"]}')

        B = '***CONCESSIONARIA***   '
        C = '                  ***GERADOR***'
        D = '                  ***OPERACÃO***'
        E = '                  ***AR COND***'

        valor_final1 =  (
          'PG  'f'       {B}\n\
          {rr}{items[0]["name"]} = {items[0]["lastvalue"]}v\n\
          {rr}{items[4]["name"]} = {items[4]["lastvalue"]}v\n\
          {rr}{items[6]["name"]} = {items[6]["lastvalue"]}v\n\
                    \n{C}\n\
          {ss}{items[1]["name"]} = {items[1]["lastvalue"]}v\n\
          {ss}{items[2]["name"]} = {items[2]["lastvalue"]}v\n\
          {ss}{items[3]["name"]} = {items[3]["lastvalue"]}v\n\
                  \n{D}\n\
          {oo}{items[5]["name"]} = {items[5]["lastvalue"]}v\n\
          {oo}{items[7]["name"]} = {items[7]["lastvalue"]}v\n\
                \n{E}\n\
          {gg}{arpg[15]["name"]} = {arpg[15]["lastvalue"]}°C\n\
          {gg}{arpg[16]["name"]} = {arpg[16]["lastvalue"]}°C\n\
          {gg}{arpg1[1]["name"]} = {arpg1[1]["lastvalue"]}°C\n\
          {gg}{arpg1[2]["name"]} = {arpg1[2]["lastvalue"]}°C\n\
          {gg}{arpg1[3]["name"]} = {arpg1[3]["lastvalue"]}°C\n\
          {gg}{arpg1[4]["name"]} = {arpg1[4]["lastvalue"]}°C\n\
              ')

        zapi.logout()
        return valor_final1


    if identificador == 10370:
        items = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': identificador
        })




        ## AR CONDICIONADO ###
        argj1 = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': 10357
        })

        argj2 = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': 10358
        })

        argj3 = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': 10359
        })


        B = '  ***CONCESSIONARIA***   '
        C = '                  ***GERADOR***'
        D = '                  ***OPERACÃO***'
        E = '                  ***AR COND***'

        valor_final1 =  (
          'GJ  'f'       {B}\n\
          {rr}{items[11]["name"]} = {items[11]["lastvalue"]}v\n\
          {rr}{items[12]["name"]} = {items[12]["lastvalue"]}v\n\
          {rr}{items[13]["name"]} = {items[13]["lastvalue"]}v\n\
              \n{C}\n\
          {ss}{items[0]["name"]} = {items[0]["lastvalue"]}v\n\
          {ss}{items[1]["name"]} = {items[1]["lastvalue"]}v\n\
          {ss}{items[2]["name"]} = {items[2]["lastvalue"]}v\n\
          {ss}{items[8]["name"]} = {items[8]["lastvalue"]}v\n\
          {ss}{items[9]["name"]} = {items[9]["lastvalue"]}v\n\
          {ss}{items[10]["name"]} = {items[10]["lastvalue"]}v\n\
              \n{D}\n\
          {oo}{items[6]["name"]} = {items[6]["lastvalue"]}v\n\
          {oo}{items[7]["name"]} = {items[7]["lastvalue"]}v\n\
                \n{E}\n\
          {gg}{argj1[0]["name"]}1 = {argj1[0]["lastvalue"]}°C\n\
          {gg}{argj1[2]["name"]}1 = {argj1[2]["lastvalue"]}°C\n\
          {gg}{argj2[0]["name"]}2 = {argj2[0]["lastvalue"]}°C\n\
          {gg}{argj2[2]["name"]}2 = {argj2[2]["lastvalue"]}°C\n\
          {gg}{argj3[0]["name"]}3 = {argj3[0]["lastvalue"]}°C\n\
          {gg}{argj3[2]["name"]}03 = {argj3[2]["lastvalue"]}°C\n ')

        zapi.logout()
        return valor_final1

    if identificador == 10524:
        items = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': identificador
        })

        # print(items)



        ##AR CONDICIONADO ###
        arbtg = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': 10378
        })

        print(arbtg)



        B = '***CONCESSIONARIA***   '
        C = '                  ***GERADOR***'
        D = '                  ***OPERACÃO***'
        E = '                  ***AR COND***'

        valor_final1 =  (
          'BTG  'f'       {B}\n\
          {rr}{items[11]["name"]} = {items[11]["lastvalue"]}v\n\
          {rr}{items[12]["name"]} = {items[12]["lastvalue"]}v\n\
          {rr}{items[13]["name"]} = {items[13]["lastvalue"]}v\n\
              \n{C}\n\
          {ss}{items[0]["name"]} = {items[0]["lastvalue"]}v\n\
          {ss}{items[1]["name"]} = {items[1]["lastvalue"]}v\n\
          {ss}{items[2]["name"]} = {items[2]["lastvalue"]}v\n\
          {ss}{items[8]["name"]} = {items[8]["lastvalue"]}v\n\
          {ss}{items[9]["name"]} = {items[9]["lastvalue"]}v\n\
          {ss}{items[10]["name"]} = {items[10]["lastvalue"]}v\n\
              \n{D}\n\
          {oo}{items[6]["name"]} = {items[6]["lastvalue"]}v\n\
          {oo}{items[7]["name"]} = {items[7]["lastvalue"]}v\n\
                \n{E}\n\
          {gg}{arbtg[0]["name"]} = {arbtg[0]["lastvalue"]}°C\n ')

        zapi.logout()
        return valor_final1


    if identificador == 10530:
        items = zapi.item.get({
            'output':['name','lastvalue'],
            'hostids': identificador
        })

        print(items)


        A = '***MAQUINA 01***   '
        B = '                ***MAQUINA 02***   '
        C = '                ***MAQUINA 03***   '
        D = '                ***MAQUINA 04***   '
        E = '                ***OPERACÃO***'


        valor_final1 =  (
          'STS  'f'       {A}\n\
            {oo}{items[0]["name"]} = {items[0]["lastvalue"]}\n\
            {rr}{items[20]["name"]} = {items[20]["lastvalue"]}\n\
            {vv}{items[21]["name"]} = {items[21]["lastvalue"]}\n\
            {cc}{items[22]["name"]} = {items[22]["lastvalue"]}\n\
            {cc}{items[23]["name"]} = {items[23]["lastvalue"]}\n\
                         \n{B}\n\
            {oo}{items[1]["name"]} = {items[1]["lastvalue"]}\n\
            {rr}{items[24]["name"]} = {items[24]["lastvalue"]}\n\
            {vv}{items[25]["name"]} = {items[25]["lastvalue"]}\n\
            {cc}{items[8]["name"]} = {items[8]["lastvalue"]}\n\
            {cc}{items[9]["name"]} = {items[9]["lastvalue"]}\n\
                        \n{C}\n\
            {oo}{items[2]["name"]} = {items[2]["lastvalue"]}\n\
            {rr}{items[10]["name"]} = {items[10]["lastvalue"]}\n\
            {vv}{items[11]["name"]} = {items[11]["lastvalue"]}\n\
            {cc}{items[12]["name"]} = {items[12]["lastvalue"]}\n\
            {cc}{items[13]["name"]} = {items[13]["lastvalue"]}\n\
                        \n{D}\n\
            {oo}{items[3]["name"]} = {items[3]["lastvalue"]}v\n\
            {rr}{items[14]["name"]} = {items[14]["lastvalue"]}\n\
            {vv}{items[15]["name"]} = {items[15]["lastvalue"]}\n\
            {cc}{items[16]["name"]} = {items[16]["lastvalue"]}\n\
            {cc}{items[17]["name"]} = {items[17]["lastvalue"]}\n\
                        \n{E}\n\
            {oo}{items[4]["name"]} = {items[4]["lastvalue"]}\n\
            {oo}{items[5]["name"]} = {items[5]["lastvalue"]}\n\
            {oo}{items[6]["name"]} = {items[6]["lastvalue"]}\n\
            {oo}{items[7]["name"]} = {items[7]["lastvalue"]}\n\
            {ii}{items[18]["name"]} = {items[18]["lastvalue"]}\n\
            {oo}{items[19]["name"]} = {items[19]["lastvalue"]}\n\
            {oo}{items[26]["name"]} = {items[26]["lastvalue"]}°C\n\
            {oo}{items[27]["name"]} = {items[27]["lastvalue"]}\n ')

        zapi.logout()
        return valor_final1


def statmux_filtro(comutacao):
      from zabbix_api import ZabbixAPI
      URL = 'http://xxxxxx'
      USERNAME = 'USUARIO xxxxx'
      PASSWORD = 'xxxxxxxxxxx'
      try:
          zapi = ZabbixAPI(URL, TimeouT=180)
          zapi.login(USERNAME, PASSWORD)
          print(f'conectado na API do zabbix {zapi.api_version()}')
      except Exception as err:
              print(f'falha ao conectar no servidor do Zabbix\n {err}')
          

      items = zapi.item.get({
              'output':['name','lastvalue'],
              'hostids': comutacao
          })
      

      listagem_new = list()
      listagem_final = [1,12,3,15,2,14,4,13,5,16,6,17,9,18,7,19,8,20,10,21,11]
      for puma in listagem_final:
          for valor in items[puma]['lastvalue']:
              if valor == '1':
                  valor = f'{ok}'
              else:
                  valor = f'{nok}'
              listagem_new.append(valor)

      C = (    f'                   SP{ok} POA{nok}')
      B = (  '**STATMUX SANTOS**')    
      statmux =  (
            'ST  'f'       {B}\n\
                       \n{C}\n\
              {items[1]["name"]} = {listagem_new[0]}\n\
              {items[12]["name"]} = {listagem_new[1]}\n\
              {items[3]["name"]} = {listagem_new[2]}\n\
              {items[15]["name"]} = {listagem_new[3]}\n\
              {items[2]["name"]} = {listagem_new[4]}\n\
              {items[14]["name"]} = {listagem_new[5]}\n\
              {items[4]["name"]} = {listagem_new[6]}\n\
              {items[13]["name"]} = {listagem_new[7]}\n\
              {items[5]["name"]} = {listagem_new[8]}\n\
              {items[16]["name"]} = {listagem_new[9]}\n\
              {items[6]["name"]} = {listagem_new[10]}\n\
              {items[17]["name"]} = {listagem_new[11]}\n\
              {items[9]["name"]} = {listagem_new[12]}\n\
              {items[18]["name"]} = {listagem_new[13]}\n\
              {items[7]["name"]} = {listagem_new[14]}\n\
              {items[19]["name"]} = {listagem_new[15]}\n\
              {items[8]["name"]} = {listagem_new[16]}\n\
              {items[20]["name"]} = {listagem_new[17]}\n\
              {items[10]["name"]} = {listagem_new[18]}\n\
              {items[21]["name"]} = {listagem_new[19]}\n\
              {items[11]["name"]} = {listagem_new[20]}\n ')
     
      zapi.logout()
      return statmux


def zabbix_rfgw(rfgw_cidade):
    from zabbix_api import ZabbixAPI
    URL = 'http://xxxxxx'
    USERNAME = 'USUARIO xxxxx'
    PASSWORD = 'xxxxxxxxxxx'
    try:
        zapi = ZabbixAPI(URL, TimeouT=180)
        zapi.login(USERNAME, PASSWORD)
        print(f'conectado na API do zabbix {zapi.api_version()}')
    except Exception as err:
            print(f'falha ao conectar no servidor do Zabbix\n {err}')
            
    
    ## RFGW ##
    lista = [{'SVE' : 10387,'PGE' : 10373,'GJA' : 10366,'BTG' : 10360,'STS' : 10423,}]
    for x in lista:
        if rfgw_cidade in x:
            identificador = (x[rfgw_cidade])
            
    
    items = zapi.item.get({
        'output':['name','lastvalue'],
        'hostids': identificador
    })
    zapi.logout()
    

    ## SWITCHES ##

    from zabbix_api import ZabbixAPI
    URL = 'http://xxxxxxxxxxxxx'
    USERNAME = 'USUARIO xxxxxxxxxxxxx'
    PASSWORD = 'xxxxxxxxxxxxxxx'
    try:
        zapi = ZabbixAPI(URL, TimeouT=180)
        zapi.login(USERNAME, PASSWORD)
        print(f'conectado na API do zabbix {zapi.api_version()}')
    except Exception as err:
            print(f'falha ao conectar no servidor do Zabbix\n {err}')


    lista1 = [{'SVE' : [35027,35131],'PGE' : [34504,34608],'GJA' : [35444,51105],'BTG' : [38854,38855],'STS' : [38461,38617]}]
    for x in lista1:
        if rfgw_cidade in x:
            identificador1 = (x[rfgw_cidade])
     
    items1 = zapi.item.get({
        'output':['name','lastvalue'],
        'itemids': identificador1
    })

    juntos = list()
    for x in range (len(items1)):
        rot = (float(items1[x] ['lastvalue']))/10
        juntos.append(rot)

    trafego = list()
    listagem_final_13 = list()            
    listagem_final = [0,1]
    for x in listagem_final:
        sub_new = juntos[x]
        trafego.append(sub_new)


    for b in trafego:    
        if b > 1:
              b = f'{ok}'
        else:
            b = f'{nok}'
        listagem_final_13.append(b)

    
################ codigo  ######################    
    listagem_final_1 = list()    
    listagem_final = [0,1,2,3,4,5]
    for x in listagem_final:
        for y in items[x]['lastvalue']:
            if int(y) == 1:
                  y = f'{ok}'
            else:
                y = f'{nok}'
            listagem_final_1.append(y)
    
    trafego = list()
    listagem_final_11 = list()            
    listagem_final = [7,8,9,10]
    for x in listagem_final:
        sub_new = items[x]['lastvalue']
        trafego.append(sub_new)
            
        if int(sub_new) > 500:
              sub_new = f'{ok}'
        else:
            sub_new = f'{nok}'
        listagem_final_11.append(sub_new)
    
    listagem_final_12 = list()            
    y = items[6]['lastvalue']       
    if int(y) < 48:
          y = f'{ok}'
    else:
        y = f'{nok}'
    listagem_final_12.append(y)


    B = (f'{rfgw_cidade}')
    C = ('** STATUS **' )
    E = ('              ** ROTA MAIN **' )
    F = ('              ** ROTA BKP **' )    
    city_new =  (f'\
              { B}\n\
                  {C}  \n\
        {items[0]["name"]} = {listagem_final_1[0]}\n\
        {items[1]["name"]} = {listagem_final_1[1]}\n\
        {items[2]["name"]} = {listagem_final_1[2]}\n\
        {items[3]["name"]} = {listagem_final_1[3]}\n\
        {items[4]["name"]} = {listagem_final_1[4]}\n\
        {items[5]["name"]} = {listagem_final_1[5]}\n\
        {items[6]["name"]} = {items[6]["lastvalue"]}°C {listagem_final_12[0]}\n\
            \n{E}\n\
        {B}SWHVID01 RX {juntos[0]}Gb{listagem_final_13[0]}\n\
        {items[7]["name"]} - v835 = {trafego[0]}Mb {listagem_final_11[0]}\n\
        {items[9]["name"]} - v836 = {trafego[2]}Mb {listagem_final_11[2]}\n\
            \n{F}\n\
        {B}SWHVID02 RX {(str(juntos[1]))[0:6]}Gb{listagem_final_13[1]}\n\
        {items[8]["name"]} - v835 = {trafego[1]}Mb {listagem_final_11[1]}\n\
        {items[10]["name"]} - v836 = {trafego[3]}Mb {listagem_final_11[3]}\n ')                        
                                    
    zapi.logout()
    return city_new

def zabbix_canais_fora(text1):
    from zabbix_api import ZabbixAPI
    URL = 'http://xxxxxxxxxxxxxx'
    USERNAME = 'USUARIO xxxxxxxxxxx'
    PASSWORD = 'xxxxxxxxxxxxxxxxx'
    try:
        zapi = ZabbixAPI(URL, TimeouT=180)
        zapi.login(USERNAME, PASSWORD)
        print(f'conectado na API do zabbix {zapi.api_version()}')
    except Exception as err:
            print(f'falha ao conectar no servidor do Zabbix\n {err}')
            
    import time
    from datetime import datetime
    b =int(time.time())    
    ontem = (b-43200)
    
            
    items = zapi.item.get({
    'output':['name','itemid'],
    'hostids': 10519
    })
    
    hora1 = []
    hora2 = []
    
    for x in range(len(items)):
        b = (items[x])
           
        items1 = zapi.history.get({
                "output": 'extend',
                "history": 3,
                "itemids": b['itemid'],
                "time_from": ontem                                 
        })
               
        hora = []
        contff = 0
        for value in items1:
            
            if value['value'] == '2':
                contff = contff + 1
                qix = (str(datetime.fromtimestamp(int(value['clock']))))
                qix1 = qix[11:]
                hora.append(qix1)
                nomecanal = f'{tv}{b["name"]} {contff}x'
                
        if contff != 0:          
            hora.insert(0,nomecanal)
            hora1.append(hora)
    time.sleep(3)
    for timer_new1 in hora1:
        for timer_new in timer_new1:
            hora2.append(timer_new)

    junior = (','.join(hora2))
    ## variavel news é a lista no formato relatório
    news = junior.replace(',' ,'\n')
    zapi.logout()
    if len(news) > 0:
        print('TEM erro FILTRO')
        return(news)
    else:
        news = (f'{feliz} não houve oscilações!!')
        print('SEM erro FILTRO')
        return(news)


def node_filtro(text1,text2,timer):
    from zabbix_api import ZabbixAPI
    URL = 'http://xxxxxxxxxxxxxxxxx'
    USERNAME = 'USUARIO xxxxxxxxxxxxxxxxx'
    PASSWORD = 'xxxxxxxxxxxxxxxxxxx'
    try:
        zapi = ZabbixAPI(URL, TimeouT=180)
        zapi.login(USERNAME, PASSWORD)
        
        print(f'conectado na API do zabbix {zapi.api_version()}')
    except Exception as err:
            print(f'falha ao conectar no servidor do Zabbix\n {err}')

    cidades = {'STS':25,'GJA':28,
               'PGE':30,'SVE':26,
               'CBT':29,'BTG':31,
               }
    print('deu certo')
    if text1 in cidades:
        city = (cidades[text1])

    itemid = zapi.host.get({
            'output':'hostid',
            'groupids': city
        })
    
    
    f = list()
    for x in itemid:
        bruno = x['hostid']
        f.append(bruno)

    itemid1 = zapi.item.get({
            'output':['name'],
            'hostids': f
        })

    sorted_list = sorted(itemid1, key=lambda k: k['name']) 

    zbx_server = 'http://xxxxxxxxxxxxxx'
    zbx_user = 'USUARIO xxxxxxxxxxxxxxx'
    zbx_pass = 'xxxxxxxxxxxxxxxxxx'
    
    loginpage = requests.get(f'{zbx_server}/index.php', auth=(zbx_user, zbx_pass), verify=False).text
    enter = re.search('<button.*value=".*>(.*?)</button>', loginpage)
    s = requests.Session()
    
    enter = str(enter.group(1))
    s.post(f'{zbx_server}/index.php?login=1', params={'name': zbx_user, 'password': zbx_pass, 'enter': enter},verify=False).text
    
    listinha = list()
    for x in sorted_list:
        if text2 in x['name']:
            # print(x['name'],'==',x['itemid'])
            itemids = x['itemid']
            #nameids = x['name']
            # print(itemids)
            listinha.append(itemids)
            
            #timer = '3'    
            #url1 = f'{zbx_server}/chart.php?from=now-{timer}h&to=now&itemids%5B0%5D={itemids}&type=0&profileIdx=web.item.graph.filter&profileIdx2=40583&width=1200&height=250&_=v3a45mlg'
            #url1 = f'{zbx_server}/chart3.php?&name={nameids} ({timer})&from=now-{timer}-0m&to=now&width=900&height=200&graphtype=1&legend=1&percent_left=0&percent_right=0&ymin_type=1&ymax_type=1&yaxismin=-30&yaxismax=0&ymin_itemid=0&ymax_itemid=0&showworkperiod=0&showtriggers=0&i%5B0%5D=gi%3A36770%2Cit%3A{itemids}%2Cso%3A0%2Cfl%3A0%2Cty%3A0%2Cdr%3A5%2Cya%3A0%2Cca%3A2%2Cdr%3A5%2Cya%3A0%2Cco%3AC2185B'
            url1 = f'{zbx_server}/chart.php?from=now-{timer}&to=now&itemids%5B0%5D={itemids}&type=0&profileIdx=web.item.graph.filter&profileIdx2={itemids}&width=900&height=200&_=v3q7w734'
            get_graph = s.get(url1)
            
            with open(f'GRACONCA/{itemids}.png', 'wb') as f:
                f.write(get_graph.content)

    chamada = len(listinha)            
    
    if chamada == 0:
        zapi.logout()
        return chamada
    if chamada == 1:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png')])
        cv2.imwrite(f"GRACOLETA/{text2}.png",img)
        zapi.logout()
        return chamada
    if chamada == 2:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png')])
        cv2.imwrite(f"GRACOLETA/{text2}.png",img)
        zapi.logout()
        return chamada
    if chamada == 3:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png')])
        cv2.imwrite(f"GRACOLETA/{text2}.png",img)
        zapi.logout()
        return chamada
    if chamada == 4:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png'),cv2.imread(f'GRACONCA/{listinha[3]}.png')])
        cv2.imwrite(f"GRACOLETA/{text2}.png",img)
        zapi.logout()
        return chamada
    if chamada == 5:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png'),cv2.imread(f'GRACONCA/{listinha[3]}.png'),cv2.imread(f'GRACONCA/{listinha[4]}.png')])
        cv2.imwrite(f"GRACOLETA/{text2}.png",img)
        zapi.logout()
        return chamada
    if chamada == 6:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png'),cv2.imread(f'GRACONCA/{listinha[3]}.png'),cv2.imread(f'GRACONCA/{listinha[4]}.png'),cv2.imread(f'GRACONCA/{listinha[5]}.png')])
        cv2.imwrite(f"GRACOLETA/{text2}.png",img)
        zapi.logout()
        return chamada
    if chamada == 7:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png'),cv2.imread(f'GRACONCA/{listinha[3]}.png'),cv2.imread(f'GRACONCA/{listinha[4]}.png'),cv2.imread(f'GRACONCA/{listinha[5]}.png'),cv2.imread(f'GRACONCA/{listinha[6]}.png')])
        cv2.imwrite(f"GRACOLETA/{text2}.png",img)
        zapi.logout()
        return chamada
    if chamada == 8:
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png'),cv2.imread(f'GRACONCA/{listinha[3]}.png')])  
        cv2.imwrite(f"GRACOLETA/{text2}900.png",img)
            
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[4]}.png'),cv2.imread(f'GRACONCA/{listinha[5]}.png'),cv2.imread(f'GRACONCA/{listinha[6]}.png'),cv2.imread(f'GRACONCA/{listinha[7]}.png')])  
        cv2.imwrite(f"GRACOLETA/{text2}901.png",img)
        zapi.logout()   
        return chamada

def grafele_filtro(city,timer):
    zbx_server = 'http://xxxxxxxxxxxxx'
    zbx_user = 'USUARIO xxxxxxxxxxxxx'
    zbx_pass = 'xxxxxxxxxxxxxxxxxx'
    
    loginpage = requests.get(f'{zbx_server}/index.php', auth=(zbx_user, zbx_pass), verify=False).text
    enter = re.search('<button.*value=".*>(.*?)</button>', loginpage)
    s = requests.Session()
    
    enter = str(enter.group(1))
    s.post(f'{zbx_server}/index.php?login=1', params={'name': zbx_user, 'password': zbx_pass, 'enter': enter},verify=False).text
    
    if city == 'SVE':
        city1 = {'CPFL TENSÃO DE LINHA':['32257VAB','32258VBC','32259VCA'],
            'CPFL TENSÃO DE FASE':['32249VAN','32250VBN','32251VCN'],
            'GERADOR TENSÃO DE LINHA':['32254VAB','32255VBC','32256VCA'],
            'GERADOR TENSÃO DE FASE':['32246VAN','32247VBN','32248VCN'],
            'AR CONDICIONADO MAQ':['43415001','43418002','43421003']       
            }

    elif city == 'PGE':
        city1 = {'CPFL TENSÃO DE LINHA':['32238VAB','32242VBC','32244VCA'],           
                'GERADOR TENSÃO DE LINHA':['32239VAB','32240VBC','32241VCA'],           
                'AR CONDICIONADO MAQ':['42981001','42985002','32283001','32284002','32285003','32286004']       
                }
        
    elif city == 'GJA':
        city1 = {'CPFL TENSÃO DE LINHA':['32235VAB','32236VBC','32237VCA'],
            'CPFL TENSÃO DE FASE':['32227VAN','32228VBN','32229VCN'],
            'GERADOR TENSÃO DE LINHA':['32232VAB','32233VBC','32234VCA'],
            'GERADOR TENSÃO DE FASE':['32224VAN','32225VBN','32226VCN'],
            'AR CONDICIONADO MAQ':['32175001','32178002','32181003']       
            }
    elif city == 'BTG':
        city1 = {'CPFL TENSÃO DE LINHA':['42833VAB','42834VBC','42835VCA'],
            'CPFL TENSÃO DE FASE':['42825VAN','42826VBN','42827VCN'],
            'GERADOR TENSÃO DE LINHA':['42830VAB','42831VBC','42832VCA'],
            'GERADOR TENSÃO DE FASE':['42822VAN','42823VBN','42824VCN'],
            'AR CONDICIONADO MAQ':['32277001','NAOENADA','NAOENADA']       
            }
        
    timer = timer.lower()
    print(timer)
    listinha = list()
    for x in city1:
        for number in city1[x]:
            itemids1 = number
            itemids2 = (number[-3:])
            itemids = itemids1[:-3]
            listinha.append(itemids)
            #time.sleep(0.2 )
            
            url1 = f'{zbx_server}/chart.php?from=now-{timer}&to=now&itemids%5B0%5D={itemids}&type=0&profileIdx=web.item.graph.filter&profileIdx2={itemids}&width=700&height=150&_=v3qnrsjr&screenid='
                        
            get_graph = s.get(url1)
            
            with open(f'GRACONCA/{itemids}.png', 'wb') as f:
                    f.write(get_graph.content)
    
    if city == 'SVE' or city == 'GJA':    
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png'),cv2.imread(f'GRACONCA/{listinha[3]}.png'),cv2.imread(f'GRACONCA/{listinha[4]}.png'),cv2.imread(f'GRACONCA/{listinha[5]}.png')])
        cv2.imwrite('GRACOLETA/CPFL.png',img)
        
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[6]}.png'),cv2.imread(f'GRACONCA/{listinha[7]}.png'),cv2.imread(f'GRACONCA/{listinha[8]}.png'),cv2.imread(f'GRACONCA/{listinha[9]}.png'),cv2.imread(f'GRACONCA/{listinha[10]}.png'),cv2.imread(f'GRACONCA/{listinha[11]}.png')])
        cv2.imwrite('GRACOLETA/GERA.png',img)
        
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[12]}.png'),cv2.imread(f'GRACONCA/{listinha[13]}.png'),cv2.imread(f'GRACONCA/{listinha[14]}.png')])
        cv2.imwrite('GRACOLETA/TEMP.png',img)
        return timer
        
    if city == 'PGE':    
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png')])
        cv2.imwrite('GRACOLETA/CPFL.png',img)
        
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[3]}.png'),cv2.imread(f'GRACONCA/{listinha[4]}.png'),cv2.imread(f'GRACONCA/{listinha[5]}.png')])
        cv2.imwrite('GRACOLETA/GERA.png',img)
        
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[6]}.png'),cv2.imread(f'GRACONCA/{listinha[7]}.png'),cv2.imread(f'GRACONCA/{listinha[8]}.png'),cv2.imread(f'GRACONCA/{listinha[9]}.png'),cv2.imread(f'GRACONCA/{listinha[10]}.png'),cv2.imread(f'GRACONCA/{listinha[11]}.png')])
        cv2.imwrite('GRACOLETA/TEMP.png',img)
        return timer
        
    if city == 'BTG':    
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[0]}.png'),cv2.imread(f'GRACONCA/{listinha[1]}.png'),cv2.imread(f'GRACONCA/{listinha[2]}.png'),cv2.imread(f'GRACONCA/{listinha[3]}.png'),cv2.imread(f'GRACONCA/{listinha[4]}.png'),cv2.imread(f'GRACONCA/{listinha[5]}.png')])
        cv2.imwrite('GRACOLETA/CPFL.png',img)
        
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[6]}.png'),cv2.imread(f'GRACONCA/{listinha[7]}.png'),cv2.imread(f'GRACONCA/{listinha[8]}.png'),cv2.imread(f'GRACONCA/{listinha[9]}.png'),cv2.imread(f'GRACONCA/{listinha[10]}.png'),cv2.imread(f'GRACONCA/{listinha[11]}.png')])
        cv2.imwrite('GRACOLETA/GERA.png',img)
        
        img = cv2.vconcat([cv2.imread(f'GRACONCA/{listinha[12]}.png')])
        cv2.imwrite('GRACOLETA/TEMP.png',img)
        return timer