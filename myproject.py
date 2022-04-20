import requests
import unidecode
from flask import Flask, request
from filtro import zabbix_filtro
from filtro import now_filtro
from filtro import eletrica_filtro
from filtro import statmux_filtro
from filtro import zabbix_rfgw
from filtro import zabbix_canais_fora


tv = ('\U0001F4FA')
trans = ('\U0001F69A') # transporte
tempo = ('\U0000231B') # lheta
joinha = ('\U0001F44D') # joinha

gg = ('\U0001F9CA') # gelo
rr =  ('\U000026A1') #raio
ss = ('\U0001F6A8') #sirene
mm = ('\U0001F447') #mao pra baixo



app = Flask(__name__)

# ATENÇÃO - NINGUÉM ALÉM DE VOCÊ DEVE SABER ESSE TOKEN
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"  # NÃO SUBIR PARA O GITHUB
config = {'url': 'https://api.telegram.org/botxxxxxxxxxxxxxxxxxxxxxx/'}
url = (f'https://api.telegram.org/bot{TOKEN}/sendMessage')

######################  envio de arquivos  ################################

# arquivo encaminhado para o bot
def upload_file(i, file):
	global config
	formatos = {'png': {'metodo': 'sendPhoto', 'send': 'photo'},
				'text': {'metodo': 'sendDocument', 'send': 'document'} }

	return requests.get(config['url'] + formatos['text' if '.txt' in file else 'png']['metodo'], {'chat_id': i['message']['from']['id']}, files={formatos['text' if '.txt' in file else 'png']['send']: open(file, 'rb')}).text


# arquivo encaminhado para o grupo
def upload_file1(i, file):
	global config
	formatos = {'png': {'metodo': 'sendPhoto', 'send': 'photo'},
				'text': {'metodo': 'sendDocument', 'send': 'document'} }

	return requests.get(config['url'] + formatos['text' if '.txt' in file else 'png']['metodo'], {'chat_id': i['message']['chat']['id']}, files={formatos['text' if '.txt' in file else 'png']['send']: open(file, 'rb')}).text


def send_message(text, chat_id):
                url = (f'https://api.telegram.org/bot{TOKEN}/sendMessage')
                data = {'text':text,'chat_id':chat_id}
                response = requests.get(url, data=data)
                print (response.content)


############  coleta arquivo json  ##################################

@app.route('/', methods=["POST"])
def inicio():
    # pegar a mensagem que o telegram enviou
    i = request.json
    # app.logger.info(f"Chegou uma nova mensagem bruninho:{i} ")


    listnew = list()
    for chaves in i.keys():
        listnew.append(chaves)
   # app.logger.info(f"listnew {listnew}")
    mess = 'message'
    member = 'my_chat_member'
    # app.logger.info('%%%%%%%%%deu certo%%%%%%%%%%')
    if member in  listnew:
        print('ALGUEM ADD O BOT')
    if mess in listnew:
        len_new= list()
        msg_new = i['message']
        for name_1 in msg_new.keys():
            len_new.append(name_1)
        if 'text' in len_new:
                chat_id0 = i['message']['from']['id'] #bot
                chat_id1 = i['message']['chat']['id'] #grupo
                text = i['message']['text'].upper() # deixa a saida em maisucula
                first_name = i['message']['from']['first_name']
                regioes = {'NODESTS':0,'NODEPGE':1,'NODESVE':2,'NODECBT':3,'NODEBTG':4,'NODEGJA':5}
                periodo = ['1H','2H','3H','4H','5H','6H','7H','8H','9H',
                           '1D','2D','3D','4D','5D','6D','7D','8D','9D','10D',
                           '11D','12D','13D','14D','15D','16D','17D','18D','19D','20D',
                           '21D','22D','23D','24D','25D','26D','27D','28D','29D','30D'
                           ]
                regioes_new = ['PGE','GJA','SVE','BTG']

                #send_message('conseguiu!', chat_id0)
                
                ###   numero errado >>>>> 
                if chat_id1 == -'xxxxxxxxxxxxxxx':
                    #send_message('conseguiu!', chat_id1)
                    text_juntando = text.replace(' ','') # juntando o texto digitado pelo usuario
                    text_zabbix = text[1:7] # saida de text ser apenas ZABBIX
                    text_nomenow = text[1:4] # saida de text ser apenas NOW
                    text_nomedecoder = text[1:8] # saida de text ser apenas DEC0DER
                    text_nomeajuda = text[1:6] # clique ajuda
                    text_nomeaqui = text[1:5] #clique aqui p obtrer ajuda
                    gerador_nome = text[1:4]
                    gerador_cidade = text_juntando[4:7] ### mostra a cidade
                    statmux_nome = text_juntando[1:8]
                    statmux_cidade = text_juntando[8:11]
                    text_rfgw = text_juntando[1:5]
                    text_cidade1 = text_juntando[5:8]
                    text_canais = text_juntando[1:7]
                    historico_dcm = unidecode.unidecode(text_juntando[7:])
                    name_total = ['STS','PGE','GJA','SVE','BTG']
		    	



##################################  coleta zabbix    ###########################################################

                    if text_zabbix == 'ZABBIX' and len(text_juntando) == 10:
                        #send_message(f'ZABBIX - Processando.....{tempo}',chat_id0)
                        text_numero = text_juntando[7:10]
                        text1 = str(text_numero)
                        send_message(f'ZABBIX - Processando.....{tempo}',chat_id1)
                        result = zabbix_filtro(text1)
                        result2 = result
                        if len(result) > 108: #108 representa o numero de caracteres caso o canal exta dentro da funcao do zabbix
                            send_message(f'{tv} Olá {first_name} {result} {trans}', chat_id1)
                            send_message(f'Olá {first_name} Segue informações do transporte {result2[-2::]} conforme solicitado {joinha}', chat_id0)
                            upload_file(i,(f'/home/sammy/myproject/TS/{"TS" + result2[-2::]}.PNG'))
                        else:
                            send_message(f'{result}',chat_id1)




##################################  busca ajuda    ###########################################################

                    elif text_nomeajuda == 'AJUDA' or text_nomeaqui == 'AQUI':
                        upload_file1(i,('/home/sammy/myproject/AJUDA/opcoes.PNG'))


#################################    Consulta de Decoders  ######################################################


                    elif text_nomedecoder == 'DECODER':
                        send_message(f'DECODER - Processando.....{tempo}',chat_id1)
                        from filtro import decoder_filtro
                        variavel_juntandocaixa = text_juntando[8:]
                        name_caixa = decoder_filtro(variavel_juntandocaixa)
                        if len(name_caixa) < 10:
                            send_message(f'Olá {first_name} em instantes estarei te enviando INBOX informações do decoder {name_caixa} !!', chat_id1)
                            send_message( f'Olá {first_name} Segue informações do decoder {name_caixa} conforme solicitado {joinha}', chat_id0)
                            upload_file(i,(f'/home/sammy/myproject/DECODER/{name_caixa}.PNG'))
                        else:
                            send_message(f'{name_caixa}',chat_id1)






##################################  busca now    ###########################################################

                    elif text_nomenow == 'NOW':
                        send_message(f'NOW - Processando.....{tempo}',chat_id1)
                        #from filtro import now_filtro
                        variavel_juntandonow = text_juntando[4:]
                        now_juntnado = now_filtro(variavel_juntandonow)
                        if len(now_juntnado) < 15:
                            send_message(f'Olá, {first_name} em instantes estarei te enviando INBOX informações relacionada a {now_juntnado} do NOW!', chat_id1)
                            send_message( f'Olá, {first_name} Segue informações sobre {now_juntnado} conforme solicitado {joinha}', chat_id0)
                            upload_file(i,(f'/home/sammy/myproject/NOW/{now_juntnado}.PNG'))
                        else:
                            send_message(f'{now_juntnado}',chat_id1)




#################################    Consulta de statmux  ######################################################

                    elif statmux_nome == 'STATMUX' and statmux_cidade == 'STS' and len(text_juntando) == 11:
                        statmux = statmux_filtro(10548)
                        send_message(f'STATMUX - processando....{tempo}', chat_id1)
                        send_message(f'Olá, {first_name} em instantes estarei te encaminhado INBOX informações referente ao STATMUX STS!', chat_id1)
                        send_message( f'Olá, {first_name} Segue informações do STATMUX STS conforme solicitado {joinha}', chat_id0)
                        send_message(f'{statmux}', chat_id0)
		     	

##################################  GERADORES  #########################################################


                    elif gerador_nome == 'HUB' and gerador_cidade in name_total and len(text_juntando) == 7:
                        valor_final1 = eletrica_filtro(gerador_cidade)
                        send_message(f'HUB - processando....{tempo}', chat_id1)
                        send_message(f'Olá, {first_name} em instantes estarei te encaminhado INBOX informações referente ao HUB {gerador_cidade}!', chat_id1)
                        send_message( f'Olá, {first_name} Segue informações do HUB {gerador_cidade} conforme solicitado {joinha}', chat_id0)
                        send_message(f'{valor_final1}', chat_id0)


#############################################  RFGATEWAY  #########################################################################

                    elif text_rfgw == 'RFGW' and len(text_juntando) == 8 and text_cidade1 in name_total:                           
                            text1 = str(text_cidade1)
                            
                            city_new = zabbix_rfgw(text1)
                            send_message('RFGW - Processando.....',chat_id1)
                            send_message(f'Olá, {first_name} em instantes estarei te encaminhado INBOX informações referente ao RFGW {text1}!', chat_id1)                        
                            send_message( f'Olá, {first_name} Segue informações do RFGW {text1} conforme solicitado {joinha}', chat_id0)
                            send_message(f'{city_new}', chat_id0)


########################################## CANAI QUE OSCILARAM  #############################################

                    elif text_canais == 'CANAIS' and historico_dcm == 'HISTORICO' and len(text_juntando) == 16:
                        send_message(f'DCM - processando....{tempo}', chat_id1)
                        news = zabbix_canais_fora(518)
                        send_message(f'{tv} OlÁ, {first_name} em instantes estarei te encaminhado INBOX informações referente a quantidade de consultas com status down nas ultimas 6hs!', chat_id1)
                        send_message( f'OlÁ, {first_name} Segue informações dos CANAIS que oscilaram! {joinha}', chat_id0)
                        send_message(f'{news}', chat_id0)

############################################ GRAFICO ELETRICA ##############################################

                    elif gerador_nome == 'HUB' and gerador_cidade in regioes_new and (text_juntando[7:]) in periodo and len(text_juntando) < 11:
                        from filtro import grafele_filtro
                        timer = grafele_filtro(gerador_cidade,text_juntando[7:])
                        send_message(f'HUB - processando....{tempo}', chat_id1)
                        send_message(f'Olá, {first_name} em instantes estarei te encaminhado os graficos referente ao HUB {gerador_cidade}! {joinha}', chat_id1)
                        send_message( f'Olá, {first_name} Segue informações das ultimas ({timer}) do HUB {gerador_cidade} conforme solicitado {joinha}', chat_id0)                        
                        send_message( f'{mm} CPFL ({timer}) do HUB {gerador_cidade} {rr}', chat_id0)
                        upload_file(i,('GRACOLETA/CPFL.png'))
                        send_message( f'{mm} GERADOR ({timer}) do HUB {gerador_cidade} {ss}', chat_id0)
                        upload_file(i,('GRACOLETA/GERA.png'))
                        send_message( f'{mm} TEMP. ({timer}) do HUB {gerador_cidade} {gg}', chat_id0)
                        upload_file(i,('GRACOLETA/TEMP.png'))
                        


########################################## consulta graficos  #############################################

                    elif text_juntando[1:8] in regioes and (len(text_juntando[8:]) < 10 and len(text_juntando[8:]) > 3):                      
                        if text_juntando[5:8] != 'STS' and len(text_juntando) <= 12:
                            send_message(f'Esse node não se encontra na cidade de {text_juntando[5:8]} ou o período é inválidoooo {joinha}', chat_id1) 
                        else:    
                            text1 = text_juntando[5:8] ##sts ou pge ou ....
                            text2 = text_juntando[8:15] #node
                            if text_juntando[-2::] in periodo:                
                                timer = text_juntando[-2::].lower()
                                text10 = text_juntando[:-2] # eliminando o periodo
                                text2 = text10[8:]              
                            else:
                                timer = '3h'                       
                            print('###############')
                            print(text_juntando[1:8])
                            print(text_juntando[8:])
                            print(len(text_juntando[8:]))
                            print('###############')
                            from filtro import node_filtro                
                            send_message(f'NODE - Processando.....{tempo}',chat_id1)
                            chamada = node_filtro(text1,text2,timer)                        
                            if chamada > 0 and chamada <= 7 :
                                #send_message(f'Olá, {first_name} em instantes vc receberá informações das últimas ({timer}) do node solicitado {joinha}', chat_id1)
                                send_message(f'Olá, {first_name} segue gráfico das ultimas ({timer}) do node {text2} conforme solicitado {joinha}', chat_id1)
                                # print(f'GRACOLETA/{text2}.png')
                                upload_file1(i,(f'GRACOLETA/{text2}.png'))
                            elif chamada == 8:
                                #send_message(f'Olá, {first_name} em instantes vc receberá informações das últimas ({timer}) do node solicitado {joinha}', chat_id1)
                                send_message(f'Olá, {first_name} segue gráfico das ultimas ({timer}) do node {text2} conforme solicitado {joinha}', chat_id1)
                                upload_file1(i,(f'GRACOLETA/{text2}900.png'))
                                upload_file1(i,(f'GRACOLETA/{text2}901.png'))
                            else:
                                send_message(f'Esse node não se encontra na cidade de {text_juntando[5:8]} ou o período é inválido {joinha}', chat_id1)


                    


#################################  comando externo valido   ###############################################################

                    else:
                        send_message('Digite um comando válidoo, em caso de duvidas digite /ajuda',chat_id1)




#################################  comando contra intrusos   ###############################################################

                elif chat_id1 != -yyyyyyyyyyyyyy:
                    send_message( f'{first_name} entre no grupo do HeadendSTS - Consulta para obter informações!', chat_id1)


    return {"ok": True}

if __name__ == "__main__":
    app.run(host='0.0.0.0')































