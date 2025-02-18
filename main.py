# Estrutura para criar um arquivo
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
    for  j in range(len(espacosLivres)):
        novoArquivo=blocoArquivos[k]
        novoArquivo.indice=espacosLivres[j]
        if(j!=len(espacosLivres)-1):
            novoArquivo.indiceProximo=espacosLivres[j+1]
        else:
            novoArquivo.indiceProximo=0
        blocosMemoria[espacosLivres[j]]=novoArquivo
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
    for j in range(len(espacosLivres)):
        novoArquivo=blocoArquivos[k]
        novoArquivo.indice=espacosLivres[j]
        if(j!=len(espacosLivres)-1):
            novoArquivo.indiceProximo=espacosLivres[j+1]
        else:
            novoArquivo.indiceProximo=0
        blocosMemoria[espacosLivres[j]]=novoArquivo
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
    k=0
    for j in range(len(espacosLivres)-1):
        novoArquivo=blocoArquivos[k]
        novoArquivo.indice=espacosLivres[j+1]
        blocosMemoria[espacosLivres[j+1]]=novoArquivo
        k+=1
      

    return blocosMemoria

# Função de remoção
def removerArquivo(indice, blocosMemoria, estrategia):
    if indice < 0 or indice >= len(blocosMemoria):
        print("Erro: Índice inválido.")
        return blocosMemoria

    if blocosMemoria[indice] == 0:
        print("Erro: Nenhum arquivo encontrado no índice especificado.")
        return blocosMemoria

    if estrategia == "continua":
        # Remove arquivos alocados de forma contígua
        arquivo = blocosMemoria[indice]
        tamanho = 1
        while arquivo.indiceProximo != 0 and arquivo.indiceProximo < len(blocosMemoria):
            proximo_indice = arquivo.indiceProximo
            blocosMemoria[proximo_indice] = 0
            tamanho += 1
        blocosMemoria[indice] = 0
        print(f"Arquivo removido (alocação contígua). Blocos liberados: {tamanho}")

    elif estrategia == "encadeada":
        # Remove arquivos alocados de forma encadeada
        atual = indice
        while atual != -1 and atual < len(blocosMemoria):
            proximo = blocosMemoria[atual].indiceProximo
            blocosMemoria[atual] = 0
            atual = proximo
        print("Arquivo removido (alocação encadeada).")

    elif estrategia == "indexada":
        # Remove arquivos alocados de forma indexada
        if blocosMemoria[indice].dados == 'Tabela de Indices':
            indices = blocosMemoria[indice].arrayindiceProximo
            for i in indices:
                blocosMemoria[i] = 0
            blocosMemoria[indice] = 0
            print("Arquivo removido (alocação indexada).")
        else:
            print("Erro: Índice não corresponde a um bloco de índice.")

    else:
        print("Erro: Estratégia de alocação inválida.")

    return blocosMemoria

def exibirVisualmente(blocosMemoria):
    for elm in blocosMemoria:
        if(elm!=0):
            print(f"INDICE DO ARQUIVO: {elm.indice}| DADOS DO ARQUIVO: {elm.dados}| PROXIMO BLOCO A SER ALOCADO: {elm.indiceProximo}| BLOCO DE INDICES:{elm.arrayindiceProximo}")
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

    blocoArquivo0=adicionarBlocosArquivos(3,'arquivo0')
    blocosMemoria=alocacaoContinua(blocoArquivo0, blocosMemoria)
    arquivoUnitario=arquivo('Paloma')
    arquivoUnitario.indice=5
    arquivoUnitario.indiceProximo=0
    blocosMemoria[5]=arquivoUnitario
    print("\n### Alocacao Continua ###")
    exibirVisualmente(blocosMemoria)

    print("\n### Alocacao Encadeada ###")
    blocoArquivos1=adicionarBlocosArquivos(3,'arquivo1')
    blocosMemoria=alocacaoEncadeada(blocoArquivos1, blocosMemoria) 
    exibirVisualmente(blocosMemoria)

    print("\n### Alocacao Indexada ###")
    blocoArquivos2=adicionarBlocosArquivos(2,'arquivo2')
    blocosMemoria=alocacaoIndexada(blocoArquivos2, blocosMemoria) 
    exibirVisualmente(blocosMemoria)


    removerArquivo(0,blocosMemoria,'continua')

main()





