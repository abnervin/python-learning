
@echo off
:loop
    REM start text.txt
    start start c:\\Users\\Usuario\\Pictures\\estudos\\python-learning\\python-learning\\text.bat
    
    REM Aguarda 5 segundos
    timeout /t 5 /nobreak > nul 
    
    REM Volta ao início do loop
    goto :loop   

