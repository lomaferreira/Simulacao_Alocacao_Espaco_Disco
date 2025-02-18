import math
# O vetor é considerado a mémoria e cada elemento um bloco
class arquivo:
    def __init__(self,indice, dados, proximo):
        self.indice=indice
        self.dados=dados
        self.proximo=proximo

#def desfragmentacao(blocosMemoria):

#Realiza a alocação de espaço por meio da estratégia de First-fit
def alocacaoContinua(blocosDados, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    tamanhoDados=len(blocosDados)
    i=0
    while(i<tamanho):
        if(len(espacosLivres)<tamanhoDados):
            if blocosMemoria[i]==0:
                espacosLivres.append(i)
            else:
                espacosLivres=[]
        else:
            break
        i+=1
    #Ocupa os segmentos de espaços livres contínuos
    k=0
    for j in espacosLivres:
        blocosMemoria[j]=blocosDados[k]
        k+=1

    return blocosMemoria

#def alocacaoEncadeada():
# def alocacaoIndexada():

#def exibirVisualmente(blocoMemoria):

def main():
    blocosMemoria=[]
    i=5
    while(i>0):
        blocosMemoria.append(0)
        i-=1

    aux=[]
    j=3
    index=0
    prox=0
    while(j>0):
        index+=1
        aux.append(arquivo(prox,'nome', index))
        j-=1
        prox+=1

    novoVetor=alocacaoContinua(aux, blocosMemoria)
    print("###Alocacao continua###")
    for elm in novoVetor:
        if(elm!=0):
            print(f"O indice do aquivo eh : {elm.indice} Dados do arquivo: {elm.dados} Proximo bloco a ser alocado: {elm.proximo}")
        else:
            print(f"Dado: {elm}")
main()





