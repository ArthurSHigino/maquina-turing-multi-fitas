import json
import argparse
import sys

def ler_json(arquivo):
    with open(arquivo, 'r') as file:
        return json.load(file)

def verificar_palavra(dados, palavra):
    #lógica para verificar a palavra com base nos dados do JSON
    num_fitas = dados['mt'][0]
    estados = dados['mt'][1][0]
    alfabeto = dados['mt'][2]
    
    simbolo_inicio = dados['mt'][4]
    simbolo_fim = dados['mt'][5]
    MT = dados['mt'][6]
    estado_atual = dados['mt'][7]
    estados_finais = dados['mt'][8]
    #print(num_fitas)
    #print(estados)
    #print(alfabeto)
    #print(simbolo_fim)
    #print(simbolo_inicio)
    #print (MT[5][0])
    #print (MT[0][2][1][2])
    palavra_real = [simbolo_inicio + (simbolo_fim * (sys.maxsize // 1000000000000000))] * num_fitas
    p = [1] * num_fitas
    palavra_real[0] = (simbolo_inicio + palavra + (simbolo_fim * (sys.maxsize // 1000000000000000)))   
    #print(palavra_real[0][p[0]])
    #print(len(MT))
    i=0
    #print(estados_finais[1])
    while i < len(MT):
    	contador = 0
    	#print(i)
    	if(MT[i][0] == estado_atual):
    		#print("i = " + str(i))
    		for j in range (num_fitas):
    			#print("j = " + str(j))
    			if(palavra_real[j][p[j]] == MT[i][2][j][0]):
    				contador+=1
    				#print(contador)
    			if(j==num_fitas-1) and (contador==num_fitas):
    				estado_atual = MT[i][1]
    				#print("estado atual = " + estado_atual)
    				for l in range(num_fitas):
    					#palavra_real[l][p[l]] = str(MT[i][2][l][1])
    					nova_string = palavra_real[l][:p[l]] + MT[i][2][l][1] + palavra_real[l][p[l] + 1:]
    					palavra_real[l] = nova_string
    					if(MT[i][2][l][2]=="<"):
    						if(p[l] > 0):
    							p[l]-=1
    					elif (MT[i][2][l][2]==">"):
    						p[l] += 1
    				
    				i=-1
    	#print("estado atual = " + estado_atual)
    	#print("i = " + str(i))
    	if i == len(MT)-1 and estado_atual in estados_finais:
    		print("Sim")
    	elif(i==len(MT)-1):
    		print("Nao")
  
    	i+=1
    
    

def main():
    parser = argparse.ArgumentParser(description='Verifica palavra de acordo com MT')
    parser.add_argument('arquivo', type=str, help='Arquivo JSON com informações da MT')
    parser.add_argument('palavra', type=str, help='Palavra a ser verificada pela MT')

    args = parser.parse_args()

    # Lendo o arquivo JSON
    dados = ler_json(args.arquivo)

    # Imprimindo o nome do arquivo
    #print("Arquivo lido:", args.arquivo)

    # Imprimindo a palavra lida
    #print("Palavra lida:", args.palavra)

    # Verificando a palavra usando os dados do arquivo JSON
    verificar_palavra(dados, args.palavra)


if __name__ == '__main__':
    main()
