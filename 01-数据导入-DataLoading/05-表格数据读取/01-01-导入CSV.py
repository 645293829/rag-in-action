from langchain_community.document_loaders import CSVLoader
import os

# 获取当前脚本的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
# 构建绝对文件路径
file_path = os.path.join(root_dir, "90-文档-Data", "黑悟空", "黑神话悟空.csv")

print(f"使用的文件路径: {file_path}")
print(f"文件是否存在: {os.path.exists(file_path)}")

# 第 1 部分: 基本加载 CSV 文件并打印记录
try:
    loader = CSVLoader(file_path=file_path, encoding="utf-8")
    data = loader.load()
    print("示例 1: 基本加载 CSV 文件并打印前两条记录")
    for record in data:
        print(record)
    print("-" * 80)
except Exception as e:
    print(f"加载 CSV 时出错: {e}")

# 第 2 部分: 跳过 CSV 文件的标题行并使用自定义列名
try:
    loader = CSVLoader(
        file_path=file_path,
        encoding="utf-8",
        csv_args={
            "delimiter": ",",
            "quotechar": '"',
            "fieldnames": ["种类", "名称", "说明", "等级"],
        },
    )
    data = loader.load()

    print("示例 2: 跳过标题行并使用自定义列名")
    for record in data[:2]:
        print(record)
    print("-" * 80)
except Exception as e:
    print(f"示例 2 出错: {e}")

# 第 3 部分: 指定 "Name" 列作为 source_column
try:
    loader = CSVLoader(file_path=file_path, encoding="utf-8", source_column="Name")
    data = loader.load()

    print("示例 3: 使用 'Name' 列作为主要内容来源")
    for record in data[:2]:
        print(record)
    print("-" * 80)
except Exception as e:
    print(f"示例 3 出错: {e}")

# # 第 4 部分: 使用 UnstructuredCSVLoader 加载 CSV 文件(效果很不好)
# from langchain_community.document_loaders import UnstructuredCSVLoader
# loader = UnstructuredCSVLoader(file_path=file_path)
# data = loader.load()
# print("示例 4: 使用 UnstructuredCSVLoader 加载文件")
# print(data)
# print("-" * 80)
