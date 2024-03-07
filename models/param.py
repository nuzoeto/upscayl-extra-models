import os

# Define a função para fazer a substituição nos arquivos .param
def substitute_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            # Substitui 'input' na segunda coluna
            line = line.replace('input,', 'data,', 1)
            # Substitui 'input' na terceira coluna
            line = line.replace(',input', ',data')
            file.write(line)

# Lista todos os arquivos .param no diretório atual e seus subdiretórios
for root, dirs, files in os.walk('./'):
    for file in files:
        if file.endswith('.param'):
            file_path = os.path.join(root, file)
            substitute_in_file(file_path)
