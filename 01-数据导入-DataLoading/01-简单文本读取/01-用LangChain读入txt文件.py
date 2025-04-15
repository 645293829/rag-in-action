# 读取单个txt文件
from langchain_community.document_loaders import TextLoader

# 指定编码为UTF-8
loader = TextLoader("90-文档-Data/黑悟空/黑悟空设定.txt", encoding="utf-8")
documents = loader.load()
print(documents)
