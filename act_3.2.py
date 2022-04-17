import re

print("Ingrese el nombre del archivo que deseas abrir: ")
name=input()
file=open(name)

operators = {'=':'Asignación','*':'Multiplicación','-':'Resta','/':'División','^':'Potencia','+':'Suma','<':'Less than','>':'Greaterthan'}
operators_key = operators.keys()

dataFlag=False
a=file.read()

count=0
program=a.split("\n")
for line in program:
    count=count+1
    print("Line ",count, "\n",line)

    tokens=line.split('')
    print("Token: ", tokens)
    print("Line ",count, "Detalles \n")
    for token in tokens:
        if token in operators_key:
            print (token,operators[token])

    dataFlag=False
    print('-------------------------------------------')
