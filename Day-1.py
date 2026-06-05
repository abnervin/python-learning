# Algoritimo anti-invasão

import os #importa a biblioteca os para executar comandos do sistema operacional

senha =input ('digite a senha: ')
if senha == '123456':
    print ('Acesso permitido')
else:
    print ('Acesso negado!!!')
    os.system('start c:\\Users\\Usuario\\Pictures\\estudos\\python-learning\\python-learning\\Arquivo.bat')