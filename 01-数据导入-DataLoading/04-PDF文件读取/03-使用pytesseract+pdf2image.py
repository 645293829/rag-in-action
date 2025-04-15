# 扫描图片型 PDF，建议用 pytesseract + pdf2image  
# sudo apt-get install tesseract-ocr
# sudo apt-get install tesseract-ocr-chi-sim

import pdf2image
import pytesseract
import os

# 将 PDF 转换为图片并保存
images = pdf2image.convert_from_path('90-文档-Data/黑悟空/黑神话悟空.pdf')
for i, image in enumerate(images):
    image.save(f'01-数据导入-DataLoading/04-PDF文件读取/output/page_{i+1}.png')

# 使用 pytesseract 提取文本
for i, image in enumerate(images):
    # 使用中文简体语言包进行识别，如果要使用英文，则去掉lang
    text = pytesseract.image_to_string(image, lang='chi_sim')
    print(f"第 {i+1} 页文本:")
    print(text)
    print("\n") 