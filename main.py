# Estrutura para criar um arquivo, considera-se -1 como vazios
class arquivo:
    def __init__(self, dados):
        self.indice=-1
        self.dados=dados
        self.extensao=-1
        self.indiceProximo=-1
        self.arrayindiceProximo=[]

#Realiza a alocação de espaço por meio da estratégia de First-fit(1º segmento diponivel é selecionado)
def alocacaoContinua(blocoArquivos, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    tamanhoDados=len(blocoArquivos)
    i=0
    while(i<tamanho):
        #Ver se já possui espaço suficiente, se não adiciona um endereço de um bloco livre
        if(len(espacosLivres)<tamanhoDados):
            if blocosMemoria[i]==-1:
                espacosLivres.append(i)
            else:
                espacosLivres=[] #Se ainda não possuir espaço suficiente e encontrar um espaço não livre no meio, esvazia os endereços para manter blocos contínuos
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
        blocosMemoria[espacosLivres[j]]=novoArquivo #Adiciona no bloco na mémoria
        k+=1
    
    blocosMemoria[espacosLivres[0]].extensao=len(espacosLivres) #Adiciona a extensão do bloco de arquivo
    return blocosMemoria

#Realiza a alocação de forma encadeada, cada bloco de arquivo possui o endereço do bloco seguinte
def alocacaoEncadeada(blocoArquivos, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    tamanhoDados=len(blocoArquivos)
    i=0
    #Busca espaços livres no disco
    while(i<tamanho):
        #Ver se já possui espaço suficiente, se não adiciona um endereço de um bloco livre
        if(len(espacosLivres)<tamanhoDados):
            if blocosMemoria[i]==-1:
                espacosLivres.append(i) # Colocar endereços livres independente de estarem fragmentados
        else:
            break
        i+=1

    # Se não houver espaços suficientes, retorna um erro
    if len(espacosLivres) < tamanhoDados:
        print("Erro: Espaco insuficiente para alocar os arquivos na alocacao encadeada")
        return blocosMemoria 

    #Ocupa os segmentos de espaços livres ainda que fragmentados
    k=0
    for j in range(len(espacosLivres)):
        novoArquivo=blocoArquivos[k]
        novoArquivo.indice=espacosLivres[j]
        if(j!=len(espacosLivres)-1):
            novoArquivo.indiceProximo=espacosLivres[j+1]  #O ultimo bloco não possui proximo, então seu indiceProximo continua vazio (-1)
        blocosMemoria[espacosLivres[j]]=novoArquivo  #Adiciona no bloco na mémoria
        k+=1

    return blocosMemoria

#Realiza a alocação indexada, existe um bloco de indices
def alocacaoIndexada(blocoArquivos, blocosMemoria):
    espacosLivres=[]
    tamanho=len(blocosMemoria)
    tamanhoDados=len(blocoArquivos)
    i=0
    while(i<tamanho):
        #Ver se já possui espaço suficiente(contando com o espaço para a bloco de indices), se não adiciona um endereço de um bloco livre
        if(len(espacosLivres)<=tamanhoDados):
            if blocosMemoria[i]==-1:
                espacosLivres.append(i)
        else:
            break
        i+=1

    # Se não houver espaços suficientes, retorna um erro
    if len(espacosLivres) <= tamanhoDados:
        print("Erro: Espaco insuficiente para alocar os arquivos na alocacao indexada")
        return blocosMemoria  
    
    #O primeiro espaço livre será reservado para o bloco de indices
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

def removerArquivoContinua(blocosMemoria, indiceInicio):
    tamanhoExtensao = blocosMemoria[indiceInicio].extensao #Pega o tamanho da extensão do bloco de arquivo a partir do inicial
    for i in range(tamanhoExtensao):
        blocosMemoria[i] = -1  # Libera o bloco
    return blocosMemoria

def removerArquivoEncadeada(blocosMemoria, indiceInicio):
    i = indiceInicio
    while i != -1 and i < len(blocosMemoria):
        blocoAtual = blocosMemoria[i]
        if blocoAtual == -1: #Se o arquivo já foi removido ou não existe
            break
        proximoIndice = blocoAtual.indiceProximo 
        blocosMemoria[i] = -1  # Libera o bloco
        i = proximoIndice #Atualiza o próximo bloco a ser removido
    return blocosMemoria


def removerArquivoIndexada(blocosMemoria, indiceTabela):
    if indiceTabela >= len(blocosMemoria) or blocosMemoria[indiceTabela] == -1:
        print("Erro: Índice inválido ou arquivo já removido.")
        return blocosMemoria
    
    blocoIndice = blocosMemoria[indiceTabela] 
    for indice in blocoIndice.arrayindiceProximo: #Passa pelo array de indices de cada bloco
        blocosMemoria[indice] = -1  # Libera cada bloco de dados
    
    blocosMemoria[indiceTabela] = -1  # Libera o bloco de indice
    return blocosMemoria

# Função de remoção completa
def removerArquivo(indice, blocosMemoria, alocacao):#Recebe o indice inicial/tabela de indice, disco e o tipo de alocação
    if(alocacao.lower()=='continua'):
        removerArquivoContinua(blocosMemoria,indice)
    elif(alocacao.lower()=='indexada'):
       removerArquivoIndexada(blocosMemoria,indice)
    elif(alocacao.lower()=='encadeada'):
        removerArquivoEncadeada(blocosMemoria,indice)
    else:
        print("Erro: Adicione uma estrutura válida")

#Mostrar todos os elementos do bloco de mémoria
def exibirVisualmente(blocosMemoria):
    for elm in blocosMemoria:
        if(elm!=-1): 
            print(f"INDICE DO ARQUIVO: {elm.indice}| DADOS DO ARQUIVO: {elm.dados}| EXTENSÃO DO BLOCO DE ARQUIVOS: {elm.extensao}|PROXIMO BLOCO A SER ALOCADO: {elm.indiceProximo}| BLOCO DE INDICES:{elm.arrayindiceProximo}")
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
        blocosMemoria.append(-1)
        i-=1
    #Inicia com um bloco de arquivo
    arquivoUnitario=arquivo('arquivo')
    arquivoUnitario.indice=5
    blocosMemoria[5]=arquivoUnitario
    print("!--- SIMULAÇÃO DE ALOCAÇÃO EM DISCO ---!")
    print("\n### ALOCAÇÃO - Mémoria Inicial ###")
    exibirVisualmente(blocosMemoria)

    #Adiciona arquivos com alocação continua
    blocoArquivo0=adicionarBlocosArquivos(3,'arquivo0')
    blocosMemoria=alocacaoContinua(blocoArquivo0, blocosMemoria)
    print("\n### Alocacao Continua ###")
    exibirVisualmente(blocosMemoria)
    
    #Adiciona arquivos com alocação encadeada
    print("\n### Alocacao Encadeada ###")
    blocoArquivos1=adicionarBlocosArquivos(3,'arquivo1')
    blocosMemoria=alocacaoEncadeada(blocoArquivos1, blocosMemoria) 
    exibirVisualmente(blocosMemoria)

    #Adiciona arquivos com alocação indexada
    print("\n### Alocacao Indexada ###")
    blocoArquivos2=adicionarBlocosArquivos(2,'arquivo2')
    blocosMemoria=alocacaoIndexada(blocoArquivos2, blocosMemoria) 
    exibirVisualmente(blocosMemoria)

    print("\n### REMOÇÃO ###")

    #Remove arquivos com alocação continua
    print("\n### Remoção da Alocação Contínua ###")
    removerArquivo(0,blocosMemoria,'continua')
    exibirVisualmente(blocosMemoria)

    #Remove arquivos com alocação encadeada
    print("\n### Remoção da Alocação Encadeada ###")
    removerArquivo(3,blocosMemoria,'encadeada')
    exibirVisualmente(blocosMemoria)

    #Remove arquivos com alocação indexada
    print("\n### Remoção da Alocação Indexada ###")
    removerArquivo(7,blocosMemoria,'indexada')
    exibirVisualmente(blocosMemoria)


main()





