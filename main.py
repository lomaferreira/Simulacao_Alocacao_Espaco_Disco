import math


def alocacaoContinua(tamanhoBlocosDados, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    espacoNecessario=math.ceil(tamanhoBlocosDados/tamanho)
    i=0
    while(i<tamanho):
        if(len(espacosLivres)<espacoNecessario):
            if all(elemento == 0 for elemento in blocosMemoria[i]):
                espacosLivres.append(i)
            else:
                espacosLivres=[]

        i+=1

    for j in espacosLivres:
        blocosMemoria[j]=

# def alocacaoEncadeada():

# def alocacaoIndexada():





def main():
    blocosMemoria=[]
    tamanhoBloco=5
    i=5
    while(i>0):
        blocosMemoria.append([0]*tamanhoBloco)
        i-=1
    
    print(blocosMemoria)







main()    