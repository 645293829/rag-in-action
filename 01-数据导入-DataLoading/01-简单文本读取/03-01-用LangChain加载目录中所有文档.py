from langchain_community.document_loaders import DirectoryLoader
loader = DirectoryLoader("./data/黑神话")
docs = loader.load()
print(f"文档数：{len(docs)}")  # 输出文档总数
print(docs[0])  # 输出第一个文档