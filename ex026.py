from random import randrange
import time
import termcolor
compnum= randrange(0,5+1)
efeito="-=-"*18
print(termcolor.colored(efeito,"yellow"))
print(termcolor.colored("Eu vou pensar em um número de 1 a 5. tente advinhar... ","blue"))
print(termcolor.colored(efeito,"yellow"))
usernum= int(input("Em que número eu pensei? "))

print(termcolor.colored("PROCESSANDO...","magenta"))
time.sleep(2)
if usernum == compnum:
    print(termcolor.colored(f"EXATO! estava pensando no {compnum}","red"))
else:
    print(termcolor.colored(f"ERRADO! estava pensando no {compnum}!!","red"))