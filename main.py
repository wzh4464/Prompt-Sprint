import os
import qrcode

# 读取 CSV 文件路径
csv_path = r"C:\Users\w84412722\AppData\Roaming\WeLink_Desktop\appdata\IM\w84412722\DownloadFiles\primeval_test_diff.csv"

# 设置每块最大字节数（安全上限）
MAX_CHUNK_SIZE = 2500

# 输出目录
output_dir = "qr_chunks"
os.makedirs(output_dir, exist_ok=True)

# 读取整个 CSV 文件
with open(csv_path, "r", encoding="utf-8") as f:
    csv_data = f.read()

# 将内容编码为字节
data_bytes = csv_data.encode("utf-8")

# 切片成多个数据块
chunks = [
    data_bytes[i : i + MAX_CHUNK_SIZE]
    for i in range(0, len(data_bytes), MAX_CHUNK_SIZE)
]

# 限制生成前10个
for idx, chunk in enumerate(chunks[:10]):
    # 将字节解码为字符串（忽略不可解码的尾部）
    chunk_str = chunk.decode("utf-8", errors="ignore")

    # 添加简单标识（方便拼接）
    header = f"[chunk {idx+1}/{len(chunks)}]\n"
    chunk_with_header = header + chunk_str

    # 生成二维码
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(chunk_with_header)
    qr.make(fit=True)
    img = qr.make_image()

    # 保存图像
    img_path = os.path.join(output_dir, f"qr_chunk_{idx+1}.png")
    img.save(img_path)

    print(f"✅ 保存二维码：{img_path}")

print("✅ 前10个二维码已生成。")
