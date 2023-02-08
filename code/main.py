import PySimpleGUI as sg
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('documentos.db')
cursor = conn.cursor()

# Criando a tabela "documentos" no banco de dados, caso ainda não exista
table_query = f"""
CREATE TABLE IF NOT EXISTS documentos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  local_guarda TEXT,
  num_prateleira TEXT,
  num_caixa TEXT,
  num_dossie TEXT,
  num_registro TEXT,
  data_distribuicao TEXT,
  num_volume TEXT,
  ano_arquivamento TEXT,
  proveniencia TEXT,
  assunto TEXT,
  especie TEXT,
  tipologia TEXT,
  requerente TEXT,
  observacao TEXT,
  tipo_arquivo TEXT,
  data_cadastro TEXT
)
"""
cursor.execute(table_query)

# Definição da GUI

questions = [    'Local de Guarda:',    'N° de Prateleira:',    'N° de Caixa:',    'N° de Dossiê:',    'N° de Registro:',    'Data de Distribuição:',    'N° do volume:',    'Ano do Arquivamento:',    'Proveniência:',    'Assunto:',    'Espécie:',    'Tipologia:',    'Requerente:',    'Observação:', 'Tipo do Arquivo:', 'Data de Cadastro:']
input_types = [sg.InputText() for _ in range(len(questions) - 1)]

layout = [[sg.Text(q,size=(15,1)), t] for q, t in zip(questions, input_types)] + [[sg.Submit(), sg.Cancel()]]

# Criação da Janela de exibição
window = sg.Window('Registro de documentos', layout)


while True:
    event, values = window.Read()
    if event == 'Submit':
        # Inserindo os dados preenchidos na GUI na tabela "documentos" do banco de dados
        insert_query = f"INSERT INTO documentos ({', '.join(questions)}) VALUES ({', '.join(['?' for _ in questions])})" 
        cursor.execute(insert_query, tuple(values))

        # Salvando as alterações no banco de dados
        conn.commit()

        # Exibindo mensagem de sucesso
        sg.Popup('Registro inserido com sucesso!')
    else:
         # Fechando a GUI
        break
# Fechando a conexão com o banco de dados
conn.close()
