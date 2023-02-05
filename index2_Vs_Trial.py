import PySimpleGUI as sg

score = 0

# Estrutura de Login do usuário

def login():
    sg.theme('Darkblue1')
    coluna = [
        [
            sg.Text('Digite o nome do jogador:',pad=(5,0)),
        ],
        [
            sg.Input(key= 'player',size=(25,1),background_color='white',text_color='black')
        ],
        [
            sg.Button('Entrar',key='entrar')
        ]
    ]
    layout_login = [
        [
            sg.Column(coluna)
        ],
    ]
    return sg.Window('Bem vindo ao Quiz do Py...Thão',layout_login,finalize=True)

# Estruta das perguntas
    
def p1():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Ciência \n',pad=(5,0)),
        ],
        [
            sg.Text('De onde é a invenção do chuveiro elétrico?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - França', 'group 1', key='A', enable_events=True)],
        [   sg.Radio('B - Inglaterra','group 1', key='B', enable_events=True)],
        [   sg.Radio('C - Brasil','group 1', key='C', enable_events=True)],
        [   sg.Radio('D - Austrália','group 1', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 1',layout,finalize=True)

def p2():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Futebol \n',pad=(5,0)),
        ],
        [
            sg.Text('Em qual ano o Brasil foi pentacampeão?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - 2006', 'group 4', key='A', enable_events=True)],
        [   sg.Radio('B - 2004','group 4', key='B', enable_events=True)],
        [   sg.Radio('C - 2002','group 4', key='C', enable_events=True)],
        [   sg.Radio('D - 1996','group 4', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 2',layout,finalize=True)

def p3():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Tecnologia \n',pad=(5,0)),
        ],
        [
            sg.Text('Qual a maior empresa de tecnologia do mundo ?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - Microsoft', 'group 9', key='A', enable_events=True)],
        [   sg.Radio('B - Multilaser','group 9', key='B', enable_events=True)],
        [   sg.Radio('C - Apple','group 9', key='C', enable_events=True)],
        [   sg.Radio('D - Sony','group 9', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 3',layout,finalize=True)

def p4():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Tecnologia \n',pad=(5,0)),
        ],
        [
            sg.Text('Qual foi o primeiro computador digital eletrônico inventado?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - Sevastopol', 'group 11', key='A', enable_events=True)],
        [   sg.Radio('B - ENIAC','group 11', key='B', enable_events=True)],
        [   sg.Radio('C - APOLLO','group 11', key='C', enable_events=True)],
        [   sg.Radio('D - EVAC','group 11', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 4',layout,finalize=True)

def p5():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Ciência \n',pad=(5,0)),
        ],
        [
            sg.Text('Atualmente, quantos elementos químicos a tabela periódica possui?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - 113', 'group 12', key='A', enable_events=True)],
        [   sg.Radio('B - 109','group 12', key='B', enable_events=True)],
        [   sg.Radio('C - 108','group 12', key='C', enable_events=True)],
        [   sg.Radio('D - 118','group 12', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 5',layout,finalize=True)

def p6():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Inglês \n',pad=(5,0)),
        ],
        [
            sg.Text('O que a palavra legend significa em português?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - Legenda', 'group 13', key='A', enable_events=True)],
        [   sg.Radio('B - Lenda','group 13', key='B', enable_events=True)],
        [   sg.Radio('C - Legendário','group 13', key='C', enable_events=True)],
        [   sg.Radio('D - Conto','group 13', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 6',layout,finalize=True)

def p7():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: História \n',pad=(5,0)),
        ],
        [
            sg.Text('Em que período da pré-história o fogo foi descoberto?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - Neolítico', 'group 17', key='A', enable_events=True)],
        [   sg.Radio('B - Paleolítico','group 17', key='B', enable_events=True)],
        [   sg.Radio('C - Idade dos Metais','group 17', key='C', enable_events=True)],
        [   sg.Radio('D - Período da Pedra Polida','group 17', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 7',layout,finalize=True)

def p8():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Astronomia \n',pad=(5,0)),
        ],
        [
            sg.Text('Qual o maior planeta do sistema solar?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - Marte', 'group 18', key='A', enable_events=True)],
        [   sg.Radio('B - Júpiter','group 18', key='B', enable_events=True)],
        [   sg.Radio('C - Terra','group 18', key='C', enable_events=True)],
        [   sg.Radio('D - Lua','group 18', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 8',layout,finalize=True)
     
def p9():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Astronomia \n',pad=(5,0)),
        ],
        [
            sg.Text('Quanto tempo a Terra demora para dar uma volta completa em torno dela mesma?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - Aproximadamente 24 horas', 'group 20', key='A', enable_events=True)],
        [   sg.Radio('B - 365 dias','group 20', key='B', enable_events=True)],
        [   sg.Radio('C - 7 dias','group 20', key='C', enable_events=True)],
        [   sg.Radio('D - 365 ou 366 dias','group 20', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 9',layout,finalize=True)

def p10():
    sg.theme('DarkBlue16')
    layout = [
        [
            sg.Text('Show do Py....Thão',pad=(100,0),font='Cooper 18',text_color='yellow')
        ],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Text('Tema: Ciência \n',pad=(5,0)),
        ],
        [
            sg.Text('Quais são as fases da Lua?\n',pad=(5,0)),
        ],
        [   sg.Radio('A - Nova, cheia e superlua', 'group 14', key='A', enable_events=True)],
        [   sg.Radio('B - Penumbral, lunar parcial, lunar total e cheia','group 14', key='B', enable_events=True)],
        [   sg.Radio('C - Nova, cheia, minguante e lua de sangue','group 14', key='C', enable_events=True)],
        [   sg.Radio('D - Nova, crescente, cheia e minguante','group 21', key='D', enable_events=True)],
        [sg.Text("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")],
        [
            sg.Button('Enter',key='enter')
        ]
    ]
    return sg.Window('Pergunta: 10',layout,finalize=True)

# Janela Final
def final_page():
    sg.theme('Darkblue1')
    coluna = [
        [
            sg.Text('Obrigado por jogar o Quiz do Py...Thão:',pad=(5,0)),
        ],
        [
            sg.Text("Parabéns por completar o jogo sua pontuação foi {}".format(score))
        ],
        [
            sg.Text('\U0001F970'*5)
        ]
    ]
    layout_login = [
        [
            sg.Column(coluna)
        ],
    ]
    return sg.Window(' Quiz do Py...Thão',layout_login,finalize=True)



#Gerenciamento da transito de telas

janela1, janela2 = login(), None   
janela2, janela3 = None, p1
janela3, janela4 = None, p2
janela4, janela5 = None, p3
janela5, janela6 = None, p4
janela6, janela7 = None, p5
janela7, janela8 = None, p6
janela8, janela9 = None, p7
janela9, janela10 = None, p8
janela10, janela11 = None, p9
janela11, janela12 = None, p10
janela12 = final_page


#Estrutura de validação de resposta
   
while True:
    window, evento, valor = sg.read_all_windows()
    if window == janela1 and evento == sg.WIN_CLOSED or window == janela2 and evento == sg.WIN_CLOSED:
        break
    elif window == janela3 and evento == sg.WIN_CLOSED or window == janela4 and evento == sg.WIN_CLOSED:
        break
    elif window == janela5 and evento == sg.WIN_CLOSED or window == janela6 and evento == sg.WIN_CLOSED:
        break
    elif window == janela7 and evento == sg.WIN_CLOSED or window == janela8 and evento == sg.WIN_CLOSED:
        break
    elif window == janela9 and evento == sg.WIN_CLOSED or window == janela10 and evento == sg.WIN_CLOSED:
        break
    elif window == janela11 and evento == sg.WIN_CLOSED or window == janela12 and evento == sg.WIN_CLOSED:
        break
    


    #Login usuario

    if window == janela1 and evento == 'entrar':
            janela1.hide()
            janela2 = p1()

    #estrutura de decisão das perguntas
    #pergunta: 01
    if window == janela2 and evento == 'enter':

        if valor['C']:
            score = score + 20
            janela2.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela3 = p2()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #pergunta: 02
    if window == janela3 and evento == 'enter':
        if valor['C']:
            score = score + 20
            janela3.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela4 = p3()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #pergunta: 03
    if window == janela4 and evento == 'enter':
        if valor['A']:
            score = score + 20
            janela4.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela5 = p4()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta')

    #pergunta: 04
    if window == janela5 and evento == 'enter':
        if valor['B']:
            score = score + 20
            janela5.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela6 = p5()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #pergunta: 05
    if window == janela6 and evento == 'enter':
        if valor['D']:
            score = score + 20
            janela6.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela7 = p6()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #pergunta: 06
    if window == janela7 and evento == 'enter':
        if valor['B']:
            score = score + 20
            janela7.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela8 = p7()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #pergunta: 07
    if window == janela8 and evento == 'enter':
        if valor['B']:
            score = score + 20
            janela8.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela9 = p8()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #pergunta: 08
    if window == janela9 and evento == 'enter':
        if valor['B']:
            score = score + 20
            janela9.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela10 = p9()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))
            
    #pergunta: 09
    if window == janela10 and evento == 'enter':
        if valor['A']:
            score = score + 20
            janela10.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela11 = p10()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #pergunta: 10
    if window == janela11 and evento == 'enter':
        if valor['D']:
            score = score + 20
            janela11.hide()
            sg.popup('Resposta correta seu score é de: {}'.format(score))
            janela12 = final_page()
        else:
            score = score - 5
            sg.popup_error('Resposta incorreta seu score é de: {}'.format(score))

    #final page        
    if window == janela12 and evento == sg.WIN_CLOSED:
        break


    
        