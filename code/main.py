import PySimpleGUI as sg
import sqlite3



# Definição da página de login
layout_login = [
    [sg.Text('Nome de usuário'), sg.InputText()],
    [sg.Text('Senha'), sg.InputText(password_char='*')],
    [sg.Submit(), sg.Cancel()]
]

# Criação da janela de login
window_login = sg.Window('Página de Login', layout_login)

# Loop de leitura de eventos da página de login
event, values = window_login.Read()

# Verificação da autenticação
if event == 'Submit':
    username = values[0]
    password = values[1]
    # Verificar se o nome de usuário e senha estão corretos
    if username == 'admin' and password == 'admin':
        # Exibindo a janela de registro de documentos
        window.Show()
    else:
        sg.Popup('Nome de usuário ou senha inválidos')
else:
    sg.Popup('Login cancelado')

# Fechando a janela de login
window_login.Close()



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

questions = [    'LOCAL DE GUARDA:',    'N° DE PRATELEIRA:',    'N° DE CAIXA:',    'N° DE DOSSIÊ:',    'N° DE REGISTRO:',    'Data de distribuição:',    'Número do volume:',    'Ano do arquivamento:',    'Proveniência:',    'Assunto:',    'Espécie:',    'Tipologia:',    'Requerente:',    'Observação:', 'Tipo do arquivo:', 'Data de cadastro:']
input_types = [sg.InputText() for _ in range(len(questions) - 1)]

layout = [[sg.Text(q), t] for q, t in zip(questions, input_types)] + [[sg.Submit(), sg.Cancel()]]

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
    if event == 'Cancel' or event is None:
         # Fechando a GUI
        break
    # Fechando a conexão com o banco de dados
    conn.close()