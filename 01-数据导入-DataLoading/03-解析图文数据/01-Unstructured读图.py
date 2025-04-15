# 需要安装TesseractOCR技术引擎

from langchain_community.document_loaders import UnstructuredImageLoader

# 如果自动检测不到Tesseract路径，需要手动指定
# pytesseract.pytesseract.tesseract_cmd = r'D:\ocr\tesseract.exe'

image_path = "90-文档-Data/黑悟空/黑悟空英文.jpg"
# UnstructuredImageLoader后面是调用YOLO的小视觉模型
loader = UnstructuredImageLoader(image_path)

data = loader.load()
print(data)
