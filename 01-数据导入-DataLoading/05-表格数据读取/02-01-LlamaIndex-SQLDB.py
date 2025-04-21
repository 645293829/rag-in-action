# pip install llama_index
# pip install mysqlclient
# pip install llama-index-readers-database

# 下面的windows好像不用安装
#  sudo apt-get install libmysqlclient-dev
#  sudo apt-get install python3-dev
from llama_index.readers.database import DatabaseReader

reader = DatabaseReader(
    scheme="mysql",
    host="39.108.92.253",
    port=3306,
    user="root",
    password="huangbaoze.com",
    dbname="rag_platform"
)

query = "SELECT * FROM chunks" # 选择所有游戏场景 -> Text-to-SQL
documents = reader.load_data(query=query)

print(f"从数据库加载的文档数量: {len(documents)}")
print(documents)

# 参考文献
# https://docs.llamaindex.ai/en/stable/examples/index_structs/struct_indices/SQLIndexDemo/