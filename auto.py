import webbrowser
import pyautogui as py
import time
#abrir no google
webbrowser.open("https://www.google.com")

#tempo de espera de 2 segundos
time.sleep(2)

#pesquisando o site
py.click(x=706, y=405)
py.write('github', interval=0.1)
py.hotkey('enter')

#clicando no site
time.sleep(2) 
py.click(x=356, y=283)

#tirando o tradutor da pagina
time.sleep(2)
py.click(x=1464, y=85)

#entrando no sing in para fazer o login
time.sleep(2)
py.click(x=1305, y=111)

#acessando a parte do login
time.sleep(2)

#digitalizando email
py.click(x=846, y=285)
py.write('''EMAIL''', interval=0.1)
time.sleep(1)

#digitalizando senha
py.click(x=807, y=367)
py.write('''SENHA''', interval=0.1)

#apertando botao de login
time.sleep(1)
py.click(x=808, y=411)

#entrando na area do perfil
time.sleep(2)
py.click(x=1527, y=100)

#entrando nos repositorios
time.sleep(2)
py.click(x=1473, y=254)

#entrando na criacao de repositorio
time.sleep(4)
py.click(x=1359, y=236)

#criancao do repositorio
time.sleep(4)
py.click(x=740, y=330)
py.write('''automacao_python''', interval=0.1)

#descritivo do repositorio
time.sleep(2)
py.click(x=790, y=433)
py.write(''criacao de um repositorio e commit dele com uma automatizacao com um bot '', interval=0.1)

#funcao de usar o scroll do mouse para descer a tela
py.scroll(-750) 

#clicando para add readme
time.sleep(2)
py.click(x=446, y=368)

#add o gitgnore para arquivos python (ou uma de sua preferencia)
time.sleep(1)
py.click(x=519, y=478)
time.sleep(2)
py.write('''python''', interval=0.1)
py.doubleClick(x=658, y=595)

#add a lincensa mit (ou uma de sua preferencia)
time.sleep(2)
py.click(x=512, y=573)
py.write('''MIT''', interval=0.1)
time.sleep(2)
py.click(x=559, y=694)

#clique para confirmar a criacao do repositorio
time.sleep(2)
py.click(x=504, y=722)

#cline no botao code
time.sleep(3)
py.click(x=1027, y=278)

#copie o https do repositorio
time.sleep(2)
py.click(x=1045, y=459)

#double click para abrir o cmd fixado na barra
time.sleep(2)
py.doubleClick(x=778, y=882)

#comando para acessar a raiz do user
time.sleep(2)
py.write('''cd''', interval=0.1)
py.hotkey('enter')

#comando para acessar os documentos (deixei metade da palavra como demonstracao da tecla tab no cmd)
time.sleep(2)
py.write('''cd docu''', interval=0.1)
py.hotkey('tab')
py.hotkey('enter')

#comando para clonar o repositorio
time.sleep(4)
py.write('''git clone ''', interval=0.1)

#comando para colar o https do repositorio
time.sleep(1)
py.hotkey('ctrl', 'v')
time.sleep(2)
py.hotkey('enter')

#comando para acessar o repositorio pelas pastas
time.sleep(4)
py.write('''cd automacao_python''', interval=0.1)
py.hotkey('tab')
py.hotkey('enter')

#comando para abrir o repositorio no vscode
time.sleep(2)
py.write('''code .''', interval=0.1)
py.hotkey('enter')

#clique para maximar o vscode
time.sleep(4)
py.click(x=1238, y=88)

#clique para apertar o novo arquivo do vscode
time.sleep(4)
py.click(x=91, y=65)

#nome do arquivo e enter para acessar o arquivo dentro do vscode
time.sleep(4)
py.write('''auto.py''', interval=0.1)
py.hotkey('enter')

#criacao de uma variavel para nao fica arquivo em branco
time.sleep(4)
py.write('''deucerto = "funcionando"''', interval=0.1)

#clique para abrir o cmd novamente
time.sleep(3)
py.click(x=783, y=889)

#comando para add as alteracoes do repositorio
time.sleep(3)
py.write('''git add .''', interval=0.1)
py.hotkey('enter')

#comando para mostrar os status das alteracoes do repositorio
time.sleep(3)
py.write('''git status''', interval=0.1)
py.hotkey('enter')

#comando para commitar as alteracoes do repositorio
time.sleep(3) 
py.write('''git commit -m "finalizado"''', interval=0.1)
time.sleep(3)
py.hotkey('enter')

#comando para subir o repositorio e finalizar a automatizacao
time.sleep(3)
py.write('''git push''', interval=0.1)
py.hotkey('enter')
