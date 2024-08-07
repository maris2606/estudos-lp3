# tem arquivo e quer trazer os dados para a memória e
# transformar pro python

# ler arquivo - read
# com o caminho do arquivo
# arquivo = open("projeto_lp3/dados.txt") # retorna objeto TextIOWrapper

# carrega os dados do arquivo em memória

# só lê uma vez, se rodar mais uma vez não vai ter mais conteúdo para ler
# print(arquivo.read()) 

# le todo o conteudo do arquivo em memoria

# conteudo = arquivo.read()
# print(conteudo)
# print(conteudo.upper())

# lembrando que, quando carrega muito arquivo pesado, não pode deixar
# aberto direto
# arquivo.close()

# essa não é muito a forma usual

# usa-se bloco with, que fecha automaticamente ao sair do escopo
# só tem acesso dentro do bloco

with open('04-arquivos/dados.txt', 'r') as arquivo:
    # conteudo = arquivo.read()
    # print(conteudo)

    linhas = arquivo.readlines()
    # retorna lista com linhas
    print(linhas)
    # ['joao\n', 'jossana\n', 'millena\n', 'marisa']
    # as vezes é mais fácil só usar for

with open('04-arquivos/dados.txt', 'r') as arquivo:
    linhas = []
    
    # 'in' utilizavel nos iteráveis, considera as linhas
    for linha in arquivo: 
        linhas.append(linha.strip()) # remove o \n e espaços

    print(linhas)

# tipo de leitura
# r - read - modo de leitura - não omitir
# w - write - substitui todo o conteudo
# a - append - escreve ao final

# with open('04-arquivos/dados.txt', 'a') as arquivo:
#     arquivo.write('\njaca')
    # quando tem pass, ele não fecha

    # em arquivo geralmente não apaga
    # só marca como inativo, por ex.
    # apagar é meio trabalhoso


with open('04-arquivos/dados.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(linhas)

# ----------------------------------------------------

# with open('04-arquivos/produtos.csv', 'r') as arquivo:
    # comma separated values
    # cada coluna representa um atributo do produto
    # cada linha é um elemento

    # um arquivo pra cada tabela
    
    # é bom tratar o csv usando biblioteca 
    # pra não fazer na mão
    
    # produtos = []
    
    # # 'in' utilizavel nos iteráveis, considera as linhas
    # for produto in arquivo: 
    #     produtos.append(produto.strip().split(sep=',')) # devolve dados com nome da lista

    # print(produtos)
def obter_produtos():
    with open('04-arquivos/produtos.csv', 'r') as arquivo:
        produtos = []
        
        # 'in' utilizavel nos iteráveis, considera as linhas
        for produto in arquivo: 
            # lista com todos os dados dessa linha
            dados_produto = produto.strip().split(sep=',')

            produto = {
                'nome': dados_produto[0],
                'preco': float(dados_produto[1]),
                'marca': dados_produto[2]
            }
            produtos.append(produto)

        return produtos

def salvar_produto(nome, preco, marca):
    with open('04-arquivos/produtos.csv', 'a') as arquivo:
        linha = f'\n{nome},{preco},{marca}'
        arquivo.write(linha)

# criar abstração que faz algo
# bom separar, pq melhora manutenção
# reutilizavel


salvar_produto('banana', 10, 'feira')
print(obter_produtos())

