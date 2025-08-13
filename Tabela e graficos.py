import pandas as pd # pandas é uma biblioteca que consegue interagir com outros arquivos e o "as pd" é pra gente conseguir chamar ele no codigo de uma forma mais breve 
import plotly.express as px # biblioteca pra fazer graficos
from IPython.display import display # biblioteca pra mostrar tabelas e graficos


tabela = pd.read_csv("C:\\Users\\Usuario\\Documents\\Pedro\\git\\Cópia de ClientesBanco.csv", encoding="latin1") # pd (biblioteca pandas), .read pra ler ai _ e o tipo do arquivo e entre parenteses o caminho do arquivo
# encoding="latin1" faz python ler algumas acentuações do pt-Br
tabela = tabela.drop("CLIENTNUM", axis=1) #.drop() pra excluir ai ali o nome doq vc quer excluir e o axis=0 pra linha e axis=1 pra coluna
tabela = tabela.drop ("Sexo", axis=1) 
tabela = tabela.drop ("Mudanças Transacoes_Q4_Q1", axis=1)
tabela = tabela.drop ("Mudança Qtde Transações_Q4_Q1", axis=1)
tabela = tabela.drop ("Educação", axis=1)
tabela = tabela.drop ("Categoria Cartão", axis=1)
tabela = tabela.dropna() # exclui todas as lnhas q pelo menos um valor é vazio
#display(tabela) 
#display(tabela.info()) #fala algumas informações gerais
#display(tabela.describe().round(2)) # descreve as porcentagens e coisas do tipo e .round () vai limitar as casas dps da virgula dependendo do numero dentro do ()
qtd_categoria = tabela["Categoria"].value_counts() # mostra a qtd de cada item daquela coluna
ptc_categoria = tabela["Categoria"].value_counts(normalize=True).round(2) # esse normalize mostra em %
ptc_inatividade = tabela["Inatividade 12m"].value_counts(normalize=True).round(2)

#display (ptc_categoria, ptc_inatividade)

for i, coluna in enumerate(tabela.columns):
    fig = px.histogram(tabela, x=coluna, color="Categoria")
    nome_arquivo = f"grafico_{i}_{coluna}.html"
    fig.write_html(nome_arquivo, auto_open=False)
    print(f"Salvo: {nome_arquivo}")





