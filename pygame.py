# -*- coding: euc-kr -*-

from PIL import Image
import pillow_heif

# HEIC ������ ����
heif_file = pillow_heif.read_heif("spiderman1.heic")

# HEIC ������ PIL �̹����� ��ȯ
image = Image.frombytes(
    heif_file.mode, 
    heif_file.size, 
    heif_file.data,
    "raw",
    heif_file.mode,
    heif_file.stride,
)

# JPEG �������� ����
image.save("spiderman1.jpg", "JPEG")

