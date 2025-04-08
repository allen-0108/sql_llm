import ollama
from config import OLLAMA_MODEL, OLLAMA_HOST, SYSTEM_PROMPT
import json

class LLMHandler:
    def __init__(self):
        # 設定 Ollama 主機
        self.client = ollama.Client(host=OLLAMA_HOST)

    def generate_sql_query(self, schema, user_question):
        """生成 SQL 查詢"""
        schema_str = json.dumps(schema, ensure_ascii=False, indent=2)
        
        prompt = f"""系統：{SYSTEM_PROMPT}

資料庫結構：
{schema_str}

使用者問題：{user_question}

請只生成 SQL 查詢："""

        try:
            response = self.client.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {
                        'role': 'system',
                        'content': SYSTEM_PROMPT
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )
            # 只返回 SQL 查詢部分
            sql_query = response['message']['content'].split('```sql')[1].split('```')[0].strip()
            return sql_query
        except Exception as e:
            print(f"LLM 生成錯誤: {e}")
            raise

    def explain_results(self, query, results):
        """解釋查詢結果"""
        results_str = results.to_string()
        
        prompt = f"""你是一個專業的資料分析師，請用自然語言解釋以下查詢結果。

SQL 查詢：
{query}

查詢結果：
{results_str}

請解釋這些結果："""

        try:
            response = self.client.chat(
                model=OLLAMA_MODEL,
                messages=[
                    {
                        'role': 'system',
                        'content': '你是一個專業的資料分析師，請用自然語言解釋查詢結果。'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )
            return response['message']['content']
        except Exception as e:
            print(f"LLM 解釋錯誤: {e}")
            raise 