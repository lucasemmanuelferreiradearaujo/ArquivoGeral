from datetime import datetime

class Documento:
    def __init__(self, local_guarda, num_prateleira, num_caixa, num_dossie, num_registro, data_distribuicao, num_volume, ano_arquivamento, proveniencia, assunto, especie, tipologia, requerente, observacao, tipo_arquivo):
        self.local_guarda = local_guarda
        self.num_prateleira = num_prateleira
        self.num_caixa = num_caixa
        self.num_dossie = num_dossie
        self.num_registro = num_registro
        self.data_distribuicao = data_distribuicao
        self.num_volume = num_volume
        self.ano_arquivamento = ano_arquivamento
        self.proveniencia = proveniencia
        self.assunto = assunto
        self.especie = especie
        self.tipologia = tipologia
        self.requerente = requerente
        self.observacao = observacao
        self.tipo_arquivo = tipo_arquivo
        self.data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f'Local de Guarda: {self.local_guarda}\nN° de Prateleira: {self.num_prateleira}\nN° de Caixa: {self.num_caixa}\nN° de Dossiê: {self.num_dossie}\nN° de Registro: {self.num_registro}\nData de Distribuição: {self.data_distribuicao}\nNúmero do Volume: {self.num_volume}\nAno do Arquivamento: {self.ano_arquivamento}\nProveniência: {self.proveniencia}\nAssunto: {self.assunto}\nEspécie: {self.especie}\nTipologia: {self.tipologia}\nRequerente: {self.requerente}\nObservação: {self.observacao}\nTipo do Arquivo: {self.tipo_arquivo}\nData de Cadastro: {self.data_cadastro}'

tipos_arquivo = ["CÓPIA", "ORIGINAL", "RASCUNHO", "MINUTA"]

documento = Documento("Biblioteca", "A1", "2", "3", "4", "05/02/2023", "5", "2022", "Ministério Público", "Processo Judicial", "Processual", "Petição", "João da Silva", "Nenhuma", tipos_arquivo[1])

print(documento)
