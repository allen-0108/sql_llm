import streamlit as st
from database import DatabaseManager
from llm_handler import LLMHandler
import pandas as pd
import warnings

# 忽略特定警告
warnings.filterwarnings("ignore", category=RuntimeWarning)

# 設定頁面配置
st.set_page_config(
    page_title="SQL LLM 查詢系統",
    page_icon="🔍",
    layout="wide"
)

# 初始化資料庫和 LLM 處理器
@st.cache_resource
def init_handlers():
    return DatabaseManager(), LLMHandler()

# 主應用程式
def main():
    st.title("🔍 SQL LLM 查詢系統")
    st.write("使用自然語言查詢您的資料庫")

    # 初始化處理器
    db_manager, llm_handler = init_handlers()

    # 側邊欄：顯示資料庫結構
    with st.sidebar:
        st.header("資料庫結構")
        try:
            schema = db_manager.get_schema()
            for table in schema:
                with st.expander(f"📊 {table['table_name']}"):
                    for col in table['columns']:
                        st.write(f"- {col['name']} ({col['type']})")
        except Exception as e:
            st.error(f"無法獲取資料庫結構: {e}")

    # 主要內容區域
    user_question = st.text_input("請輸入您的問題：", placeholder="例如：顯示所有客戶的訂單總金額")

    if user_question:
        with st.spinner("正在處理您的查詢..."):
            try:
                # 生成 SQL 查詢
                sql_response = llm_handler.generate_sql_query(schema, user_question)
                
                # 顯示生成的 SQL
                st.subheader("生成的 SQL 查詢")
                st.code(sql_response, language="sql")

                # 執行查詢
                results = db_manager.execute_query(sql_response)
                
                # 顯示查詢結果
                st.subheader("查詢結果")
                st.dataframe(results)

                # 解釋結果
                explanation = llm_handler.explain_results(sql_response, results)
                st.subheader("結果解釋")
                st.write(explanation)

            except Exception as e:
                st.error(f"處理查詢時發生錯誤: {e}")

    # 頁尾
    st.markdown("---")
    st.markdown("### 💡 使用提示")
    st.markdown("""
    1. 使用自然語言描述您想要查詢的內容
    2. 系統會自動生成對應的 SQL 查詢
    3. 查詢結果會以表格形式顯示
    4. 系統會自動解釋查詢結果
    """)

if __name__ == "__main__":
    main() 