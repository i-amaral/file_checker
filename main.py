import pandas as pd
from tkinter import Tk
from tkinter import filedialog

def comparar_excels(file1, file2):
    try:
        print('\nLendo os arquivos...')
        if file1 or file2 is None:
            print('Nenhum arquivo selecionado. Por favor, selecione ambos os arquivos para comparação.')
            return False
        # Lê os arquivos Excel (por padrão lê a primeira aba)
        df_dev = pd.read_excel(file1)
        df_main = pd.read_excel(file2)  
        # Compara se os DataFrames são exatamente iguais
        comparator = df_dev.equals(df_main)
        return comparator
    except Exception as e:
        print(f'Erro ao ler os arquivos: {e}')
        return False

file1 = filedialog.askopenfilename()
file2 = filedialog.askopenfilename()

result = comparar_excels(file1, file2)

print('\nOs arquivos são 100% iguais!' if result == True else '\nAtenção! Os arquivos são diferentes.')

# AJUSTAR O CÓDIGO PARA ACEITAR QUALQUER ARQUIVO, NÃO APENAS EXCEL, E COMPARAR O CONTEÚDO DE FORMA MAIS FLEXÍVEL, COMO IGNORAR ORDEM DAS LINHAS, DIFERENÇAS DE FORMATAÇÃO, ETC.
# VERIFICAR SOMENTE SE OS 2 ARQUIVOS FOREM VÁLIDOS E FOREM DO MESMO TIPO (EX: AMBOS EXCEL, AMBOS CSV, ETC.)
# FAZER O ORQUESTRADOR MAIN, QUE CHAME AS FUNÇÕES DE LEITURA E COMPARAÇÃO, E TRATE OS ERROS DE FORMA ADEQUADA, INFORMANDO O USUÁRIO SOBRE O STATUS DA OPERAÇÃO.