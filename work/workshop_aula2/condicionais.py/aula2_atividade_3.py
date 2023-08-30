vel=float(input("digite a velocidade do carro: "))
if vel>80:
    multa=vel-80
    print(f"você foi multado por passar acima do limite de velocidade, o valor da multa é de {multa*7} reais")
else:
    print("voce esta dentro do limite de velocidade.")