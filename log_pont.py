# listas
codigo =[]
tensao=[]
corrente=[]
potencia=[]
poten=0
cont_tensao=0
maior_pot=0
menor_pot=float('inf') #obs
cod_mais_eco=''
cod_menos_eco=''

# alimentando listas
for i in range (3):
    print(f'Chuveiro nº{i+1}:')
    cod=str(input('Digite o codigo do chuveiro:'))
    tens=float(input('Digite a tensão do chuveiro:'))
    corren=float(input('Digite a corrente do chuveiro:'))
    print('---------------------------------------------------------------')

    codigo.append(cod)
    tensao.append(tens)
    corrente.append(corren)

# potencia de cada chuveiro
for i in range (3):
    poten= tensao[i]*corrente[i]
    potencia.append(poten)
    print(f'A potência do chuveiro:{potencia[i]} W')
    print('---------------------------------------------------------------')

# codigos & potencias dos chuveiros
print('Codigos & Potências dos chuveiros: ')
for i in range (3):
    print(f'Codigo do chuveiro{codigo[i]} & Potência: {potencia[i]}W')
    print('---------------------------------------------------------------')

# calculo de média das potências
md_potencia= sum(potencia) / len(potencia)
print(f'Média é da potência: {md_potencia:.2f}W')
print('---------------------------------------------------------------')

#chuveiros possuem tensoes maiores que 50.
for i in range (3):
    if tensao[i] > 50:
        cont_tensao+=1
        print(f'Chuveiro do codigo {codigo[i]} com tensão maior que 50: {cont_tensao}')
        print('---------------------------------------------------------------')

# chuveiros mais e menos economicos e seus codigos de identificação

for i in range (3):
    if potencia[i] > maior_pot:
        maior_pot= potencia[i]
        cod_menos_eco=codigo[i]

    if potencia[i] < menor_pot:
        menor_pot = potencia[i]
print(f'O chuveiro do código mais econômico é:{cod_mais_eco} a sua potência é de: {menor_pot} Watts')
print(f'O chuveiro do código menos econômico é:{cod_menos_eco} a sua potência é de: {maior_pot} Watts')  

