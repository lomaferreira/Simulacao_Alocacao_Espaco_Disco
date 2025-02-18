import math
# O vetor é considerado a mémoria e cada elemento um bloco
class arquivo:
    def __init__(self, dados):
        self.indice=0
        self.dados=dados
        self.indiceProximo=0
        self.arrayindiceProximo=[]

#def desfragmentacao(blocosMemoria):


#Realiza a alocação de espaço por meio da estratégia de First-fit
def alocacaoContinua(blocoArquivos, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    tamanhoDados=len(blocoArquivos)
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

    # Se não houver espaços suficientes, retorna um erro
    if len(espacosLivres) < tamanhoDados:
        print("Erro: Espaco insuficiente para alocar os arquivos na alocacao continua")
        return blocosMemoria  
    
    #Ocupa os segmentos de espaços livres contínuos
    k=0
    for j in espacosLivres:
        novoArquivo=blocoArquivos[k]
        novoArquivo.indice=j
        novoArquivo.indiceProximo=j+1
        blocosMemoria[j]=novoArquivo
        k+=1

    return blocosMemoria

def alocacaoEncadeada(blocoArquivos, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    tamanhoDados=len(blocoArquivos)
    i=0
    while(i<tamanho):
        if(len(espacosLivres)<tamanhoDados):
            if blocosMemoria[i]==0:
                espacosLivres.append(i)
        else:
            break
        i+=1

      # Se não houver espaços suficientes, retorna um erro
    if len(espacosLivres) < tamanhoDados:
        print("Erro: Espaco insuficiente para alocar os arquivos na alocacao encadeada")
        return blocosMemoria  
    #Ocupa os segmentos de espaços livres contínuos
    k=0
    for j in espacosLivres:
        novoArquivo=blocoArquivos[k]
        novoArquivo.indice=j
        novoArquivo.indiceProximo=j+1
        blocosMemoria[j]=novoArquivo
        k+=1

    return blocosMemoria

def alocacaoIndexada(blocoArquivos, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    tamanhoDados=len(blocoArquivos)
    i=0
    while(i<tamanho):
        if(len(espacosLivres)<=tamanhoDados):
            if blocosMemoria[i]==0:
                espacosLivres.append(i)
        else:
            break
        i+=1

    # Se não houver espaços suficientes, retorna um erro
    if len(espacosLivres) <= tamanhoDados:
        print("Erro: Espaco insuficiente para alocar os arquivos na alocacao indexada")
        return blocosMemoria  
    
    blocoIndice=arquivo('Tabela de Indices')
    blocoIndice.indice=espacosLivres[0]
    blocoIndice.arrayindiceProximo=espacosLivres
    blocosMemoria[espacosLivres[0]]=blocoIndice
    #Ocupa os segmentos de espaços livres contínuos
    for j in range(len(espacosLivres)):
        posicao=espacosLivres[j]
        novoArquivo=blocoArquivos[j]
        novoArquivo.indice=posicao+1
        if(j<len(espacosLivres)-1):
            blocosMemoria[posicao+1]=novoArquivo
      

    return blocosMemoria

def exibirVisualmente(blocosMemoria):
    for elm in blocosMemoria:
        if(elm!=0):
            print(f"INDICE DO ARQUIVO: {elm.indice} DADOS DO ARQUIVO: {elm.dados} PROXIMO BLOCO A SER ALOCADO: {elm.indiceProximo} BLOCO DE INDICES:{elm.arrayindiceProximo}")
        else:
            print(f"Dado: {elm}")

def adicionarBlocosArquivos(tamanho,dados):
    blocoArquivos=[]
    j=tamanho
    while(j>0):
        blocoArquivos.append(arquivo(dados))
        j-=1
    return blocoArquivos

def main():
    #Definição da mémoria
    blocosMemoria=[]
    i=10
    while(i>0): #Inicial tudo como vazio
        blocosMemoria.append(0)
        i-=1

    blocoArquivos=[]
    j=3
    while(j>0):
        blocoArquivos.append(arquivo('nome'))
        j-=1


    novoVetor=alocacaoContinua(blocoArquivos, blocosMemoria)
    arquivoUnitario=arquivo('Paloma')
    arquivoUnitario.indice=5
    arquivoUnitario.indiceProximo=6
    novoVetor[5]=arquivoUnitario
    print("### Alocacao Continua ###")
    exibirVisualmente(novoVetor)

    print("\n### Alocacao Encadeada ###")
    arquivos=adicionarBlocosArquivos(7,'arquivo2')
    novoVetor2=alocacaoEncadeada(arquivos, novoVetor) 
    exibirVisualmente(novoVetor2)

    # print("\n### Alocacao Indexada ###")
    # arquivos2=adicionarBlocosArquivos(3,'arquivo3')
    # novoVetor3=alocacaoIndexada(arquivos2, novoVetor2) 
    # exibirVisualmente(novoVetor3)



    

main()





