import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

print("Iniciando extração do Google Sheets...")

# Caminho para o arquivo JSON de credenciais
import os

SERVICE_ACCOUNT_FILE = os.path.expanduser("~/Documents/GitHub/ABF_dash/credentials/credentials.json")

# Definir escopos de acesso
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Autenticação com a conta de serviço
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

# ID da planilha e nome da aba
SHEET_ID = "1Rsifiri4pr-4EttJHRUOitxCjOOGMCQTg5o-Bqo4dbI"
SHEET_NAME = "ALLOCATIONS"

# Função para extrair os dados e salvar como CSV
def extract_data():
    try:
        print("Acessando Google Sheets...")
        sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
        
        # Pular as primeiras 2 linhas e começar a ler da linha 3
        data = sheet.get_all_records(head=3)  
        df = pd.DataFrame(data)

        # Salvar os dados na pasta data/
        output_file = "data/extracted_data.csv"
        df.to_csv(output_file, index=False, encoding="utf-8")

        print(f"Dados extraídos com sucesso e salvos em {output_file}!")
    except Exception as e:
        print(f"Erro ao acessar a planilha: {e}")

# Executar a extração
if __name__ == "__main__":
    extract_data()
