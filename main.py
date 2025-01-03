from datetime import datetime

hoje = datetime.now()

ano = hoje.strftime("%Y")
print("Ano:",ano)

mes = hoje.strftime("%m")
print("Mês:",mes)

dia = hoje.strftime("%d")
print("Dia:",dia)

print("Dia\tMês\tAno\n{}\t{}\t{}".format(dia,mes,ano))