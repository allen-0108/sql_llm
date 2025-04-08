import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 資料庫設定
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'your_database')
}

# Ollama 設定
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'phi4')
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

# 系統提示詞
SYSTEM_PROMPT = """你是一個專業的 SQL 專家，負責將使用者的自然語言問題轉換為 SQL 查詢。
請根據提供的資料庫結構和使用者問題，生成準確的 SQL 查詢。
在回應時，請：
1. 生成正確的 SQL 查詢
2. 解釋生成的 SQL 查詢
3. 提供查詢結果的自然語言解釋""" 
