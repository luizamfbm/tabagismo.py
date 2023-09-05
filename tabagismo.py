tempo_fumando = float(input("Quantos anos você fuma? "))
valor_maco = float(input("Qual é o valor atual do maço de cigarros? R$ "))
maços_por_dia = float(input("Quantos maços de cigarros você fuma por dia? "))


dias_por_ano = 365.25  # Considerando anos bissextos
montante_gasto = tempo_fumando * dias_por_ano * maços_por_dia * valor_maco


if montante_gasto < 20000:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter dado entrada em um carro.")
elif 20000 <= montante_gasto <= 50000:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R$ {montante_gasto:.2f}, você poderia ter comprado um carro zero.")