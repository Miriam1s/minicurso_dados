import pandas as pd

# Testa leitura dos dados principais do minicurso
def testa_leitura():
    print('Testando leitura dos arquivos...')
    clientes = pd.read_csv('dados/clientes.csv')
    vendas = pd.read_csv('dados/vendas.csv')
    produtos = pd.read_csv('dados/produtos.csv')
    print('\nClientes:')
    print(clientes.head())
    print('\nVendas:')
    print(vendas.head())
    print('\nProdutos:')
    print(produtos.head())
    print('\nLeitura realizada com sucesso!')

if __name__ == '__main__':
    testa_leitura()
