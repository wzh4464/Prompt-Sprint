import os
import lzma
import base64
import qrcode
from qrcode.exceptions import DataOverflowError

# ===== 用户配置 =====
csv_path = r"data/primeval_test_diff.csv"
output_dir = "qr_lzma_chunks"
max_version = 40
max_chunk_size = 2950  # 初始尝试的最大字符数
min_chunk_size = 1000  # 不低于这个值，防止死循环
step = 25  # 每次减少多少字符尝试

# ===== 创建输出目录 =====
os.makedirs(output_dir, exist_ok=True)

# ===== 读取 CSV 文件 =====
with open(csv_path, "r", encoding="utf-8") as f:
    csv_data = f.read()

print(f"✅ 原始数据大小：{len(csv_data.encode('utf-8'))} 字节")

# ===== 使用 LZMA 压缩 + base64 编码 =====
compressed = lzma.compress(csv_data.encode("utf-8"), preset=9)
b64_data = base64.b64encode(compressed).decode("utf-8")

print(f"✅ 压缩并编码后大小：{len(b64_data)} 字符")

# ===== 动态分块并生成二维码 =====
chunks = []
start = 0
while start < len(b64_data):
    chunk_size = max_chunk_size
    success = False

    while chunk_size >= min_chunk_size:
        end = min(start + chunk_size, len(b64_data))
        chunk_data = b64_data[start:end]
        temp_text = f"[chunk ?/?]\n{chunk_data}"

        try:
            qr = qrcode.QRCode(
                version=max_version,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(temp_text)
            qr.make(fit=False)
            success = True
            break  # 找到最大能装的数据块，跳出循环
        except DataOverflowError:
            chunk_size -= step  # 缩小 chunk 再试

    if not success:
        raise RuntimeError(f"❌ 无法压缩第 {len(chunks)+1} 块：数据太大")

    # 保存成功块
    chunks.append(chunk_data)
    start += chunk_size

# ===== 生成二维码图片 =====
total_chunks = len(chunks)
print(f"✅ 最终二维码数量：{total_chunks}")

for idx, chunk in enumerate(chunks):
    header = f"[chunk {idx + 1}/{total_chunks}]\n"
    full_text = header + chunk

    qr = qrcode.QRCode(
        version=max_version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=100,
        border=3,
    )
    qr.add_data(full_text)
    qr.make(fit=False)
    img = qr.make_image()

    img_path = os.path.join(output_dir, f"qr_chunk_{idx + 1}.png")
    img.save(img_path)
    print(f"🟩 已保存：{img_path}")

print("\n✅ 所有二维码已生成完成。路径：", os.path.abspath(output_dir))
