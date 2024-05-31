# -*- coding: euc-kr -*-

from PIL import Image
import pillow_heif

# HEIC 파일을 열기
heif_file = pillow_heif.read_heif("spiderman1.heic")

# HEIC 파일을 PIL 이미지로 변환
image = Image.frombytes(
    heif_file.mode, 
    heif_file.size, 
    heif_file.data,
    "raw",
    heif_file.mode,
    heif_file.stride,
)

# JPEG 형식으로 저장
image.save("spiderman1.jpg", "JPEG")

