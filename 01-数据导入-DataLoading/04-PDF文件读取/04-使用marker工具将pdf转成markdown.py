# 使用GPU时： pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

import torch  # 添加这行导入
import os
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered



input_pdf = "90-文档-Data/山西文旅/云冈石窟/云冈石窟-en.pdf"
output_dir = "90-文档-Data/山西文旅/云冈石窟-md"
# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)


# 检查GPU是否可用并设置设备
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
converter = PdfConverter(
    artifact_dict=create_model_dict(device=device),
)
rendered = converter("90-文档-Data/山西文旅/云冈石窟-en.pdf")
text, _, images = text_from_rendered(rendered)

# 打印提取的文本
print(" 图片: ", images)
# 保存Markdown文件
output_md = os.path.join(output_dir, "云冈石窟-en.md")
with open(output_md, "w", encoding="utf-8") as f:
    f.write(text)

# 保存图片
if images:
    images_dir = os.path.join(output_dir, "")
    os.makedirs(images_dir, exist_ok=True)
    
    # 遍历图片字典，保持原始文件名
    for img_name, img_obj in images.items():
        img_path = os.path.join(images_dir, img_name)
        # 直接保存PIL.Image对象
        img_obj.save(img_path)
        print(f"图片已保存至: {img_path}")

print(f"转换完成，Markdown文件已保存至: {output_md}")