from sqlalchemy import create_engine, text
import pandas as pd

# 确保使用 pymysql 作为驱动
engine = create_engine("mysql+pymysql://root:huangbaoze.com@39.108.92.253:3306/rag_platform")

# 测试连接
try:
    with engine.connect() as connection:
        # 使用 text() 函数包装 SQL 语句
        result = connection.execute(text("SELECT * FROM chunks"))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print("查询结果：")
        print(df)
except Exception as e:
    print("数据库连接失败:", e)



