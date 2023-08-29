
idade=int(input("digite sua idade: "))
if idade>=18:
    print("parabens ja pode tirar sua CNH")
else:
    print(f"infelizmente ainda faltam {18-idade} anos ate ter idade para tirar CNH")