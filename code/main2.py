import PySimpleGUI as sg
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('documentos.db')
cursor = conn.cursor()

# Criando a tabela "documentos" no banco de dados, caso ainda não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS documentos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  local_guarda TEXT,
  num_prateleira INTEGER,
  num_caixa INTEGER,
  num_dossie INTEGER,
  num_registro INTEGER,
  data_distribuicao TEXT,
  num_volume INTEGER,
  ano_arquivamento INTEGER,
  proveniencia TEXT,
  assunto TEXT,
  especie TEXT,
  tipologia TEXT,
  requerente TEXT,
  observacao TEXT,
  tipo_arquivo TEXT,
  data_cadastro TEXT
)
""")

# Definição da GUI
layout = [    [sg.Text('LOCAL DE GUARDA:', size=(15, 1)), sg.InputText()],
    [sg.Text('N° DE PRATELEIRA:', size=(15, 1)), sg.InputText()],
    [sg.Text('N° DE CAIXA:', size=(15, 1)), sg.InputText()],
    [sg.Text('N° DE DOSSIÊ:', size=(15, 1)), sg.InputText()],
    [sg.Text('N° DE REGISTRO:', size=(15, 1)), sg.InputText()],
    [sg.Text('Data de distribuição:', size=(15, 1)), sg.InputText()],
    [sg.Text('Número do volume:', size=(15, 1)), sg.InputText()],
    [sg.Text('Ano do arquivamento:', size=(15, 1)), sg.InputText()],
    [sg.Text('Proveniência:', size=(15, 1)), sg.InputText()],
    [sg.Text('Assunto:', size=(15, 1)), sg.InputText()],
    [sg.Text('Espécie:', size=(15, 1)), sg.InputText()],
    [sg.Text('Tipologia:', size=(15, 1)), sg.InputText()],
    [sg.Text('Requerente:', size=(15, 1)), sg.InputText()],
    [sg.Text('Observação:', size=(15, 1)), sg.InputText()],
    [sg.Text('Tipo do arquivo:', size=(15, 1)),     sg.Combo(['CÓPIA', 'ORIGINAL', 'RASCUNHO', 'MINUTA'])],
    [sg.Text('Data de cadastro:', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Registro de documentos', layout)

while True:
    event, values = window.Read()
    if event == 'Submit':
        # Inserindo os dados preenchidos na GUI na tabela "documentos" do banco de dados
        cursor.execute("""
        INSERT INTO documentos (local_guarda, num_prateleira, num_caixa, num_dossie, num_registro,
        data_distribuicao, num_volume, ano_arquivamento, proveniencia, assunto, especie, tipologia,
        requerente, observacao, tipo_arquivo, data_cadastro)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (values[0], values[1], values[2], values[3], values[4], values[5], values[6],
            values[7], values[8], values[9], values[10], values[11], values[12], values[13],
            values[14], values[15]))

        # Salvando as alterações no banco de dados
        conn.commit()

        # Exibindo mensagem de sucesso
        sg.Popup('Registro inserido com sucesso!')

    if event == 'Cancel' or event is None:
    # Fechando a conexão com o banco de dados
        conn.close()

    # Fechando a GUI
    break
