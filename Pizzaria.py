print("Bem-vindo à loja de música Liandre")

print("Bem vindo a loja o que o senhor deseja, se não quiser nada digite '0'")

guitarra = int(input("1-Guitarra 10,0: "))
violão = int(input("2-Violão 12,0: "))
violino = int(input("3-Violino 10,0: "))
viola = int(input("4-Viola 15,0: "))
saxsofone = int(input("5-Saxsofone 15,0: "))
pandeiro = int(input("6-Pandeiro 12,0: "))
chocalho = int(input("7-Chocalho 12,0: "))

produto1 = guitarra * 10.00
produto2 = violão * 12.00
produto3 = violino * 10.00
produto4 = viola * 15.00
produto5 = saxsofone * 15.00
produto6 = pandeiro * 12.00
produto7 = chocalho * 12.00

Total = produto1 + produto2 + produto3 + produto4 + produto5 + produto6 + produto7

Quantidade = int(input("Escreva a quantidade de produtos que o senhor comprou."))
joros = int(input("quantos produtos o senhor comprou, se não comprou nada digite apenas 0: "))

if(joros<=0):
    print("Certo")
elif(joros>=1):
    print("Certo, um juros será cobrado ao valor final")

juros0 = 10 + joros
juros1 = juros0 + 100
juros2 = (Total + juros1) / 100
juros3 = Total + juros2

for Tempo in range(1,10,1):
    print(f"Aguarde um pouco, estamos calculando o seu pedido: {Tempo}")
print(f"O preço total em pizza será: {juros3} Reais")
print("Pedido finalizado, aguarde o pedido em seus lugares") 