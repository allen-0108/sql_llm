# SQL LLM 查詢系統

這是一個使用自然語言查詢資料庫的應用系統，結合了 LLM（大型語言模型）和 MySQL 資料庫的功能。 主要使用ollama並搭配phi4模型。

## 功能特點

- 使用自然語言進行資料庫查詢
- 自動生成 SQL 查詢語句
- 執行查詢並顯示結果
- 自動解釋查詢結果
- 支援多種資料庫表格結構

## 技術架構

- 前端：Streamlit
- 後端：Python
- 資料庫：MySQL
- LLM：Ollama（支援多種開源模型）- phi4-14B

## 安裝需求

- Python 3.8+
- MySQL 8.0+
- Ollama（用於運行本地 LLM）

## 安裝步驟

1. clone專案：
```bash
git clone https://github.com/your-username/sql_llm_system.git
cd sql_llm_system
```

2. 安裝 Python 相關套件：
```bash
pip install -r requirements.txt
```

3. 設定環境變數：
   - 複製 `.env.example` 為 `.env`
   - 修改 `.env` 檔案中的設定：
     ```
     # 資料庫設定
     DB_HOST=localhost
     DB_USER=your_username
     DB_PASSWORD=your_password
     DB_NAME=your_database

     # Ollama 設定
     OLLAMA_MODEL=phi4
     OLLAMA_HOST=http://localhost:11434
     ```

4. 安裝 Ollama：
   - 從 [Ollama 官網](https://ollama.ai/download) 下載並安裝
   - 下載模型：
     ```bash
     ollama pull phi4
     ```

## 使用方法

1. 啟動應用程式：
```bash
streamlit run app.py
```

2. 在瀏覽器中開啟 http://localhost:8501

3. 使用自然語言輸入您的查詢問題

## 專案結構

```
sql_llm_system/
├── app.py              # Streamlit 應用程式主檔案
├── config.py           # 設定檔
├── database.py         # 資料庫操作相關程式碼
├── llm_handler.py      # LLM 處理相關程式碼
├── requirements.txt    # Python 依賴套件
├── .env.example        # 環境變數範例
└── README.md           # 專案說明文件
```

## 貢獻指南

歡迎提交 Pull Request 或提出 Issue。

## 授權

MIT License 
