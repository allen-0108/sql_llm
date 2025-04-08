import mysql.connector
from config import DB_CONFIG
import pandas as pd

class DatabaseManager:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        """建立資料庫連接"""
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)
            print("成功連接到資料庫")
        except mysql.connector.Error as err:
            print(f"資料庫連接錯誤: {err}")
            raise

    def get_schema(self):
        """獲取資料庫結構"""
        if not self.connection:
            self.connect()
        
        cursor = self.connection.cursor()
        schema_info = []
        
        # 獲取所有表格
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        for table in tables:
            table_name = table[0]
            # 獲取表格結構
            cursor.execute(f"DESCRIBE {table_name}")
            columns = cursor.fetchall()
            
            schema_info.append({
                'table_name': table_name,
                'columns': [{'name': col[0], 'type': col[1], 'key': col[3]} for col in columns]
            })
        
        cursor.close()
        return schema_info

    def execute_query(self, query):
        """執行 SQL 查詢並返回結果"""
        if not self.connection:
            self.connect()
        
        try:
            # 使用 pandas 讀取查詢結果
            df = pd.read_sql(query, self.connection)
            return df
        except Exception as e:
            print(f"查詢執行錯誤: {e}")
            raise

    def close(self):
        """關閉資料庫連接"""
        if self.connection:
            self.connection.close()
            self.connection = None 