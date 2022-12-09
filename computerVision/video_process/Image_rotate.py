import os
from PIL import Image
import glob

# 이미지 폴더 불러오기
path = f"./ComputerVision/house_zip_3/toilet"
files = glob.glob(path + '/*')

# directory 생성
make_path = f"./ComputerVision/house_zip_3/toilet_rotate"
if not os.path.isdir(make_path):
    os.mkdir(make_path)

# directory 경로
save_path = f"./ComputerVision/house_zip_3/toilet_rotate/"

# 이미지 순차적으로 불러오기
for f in files:
    for idx, file in enumerate(files):
        fname, ext = os.path.splitext(file)
        if ext in ['.jpg', '.png', '.gif']:
            image = Image.open(file)
            width, height = image.size # 가로 세로 사이즈 지정
            crop_image = image.rotate(180) # 180도 회전
            crop_image.save(save_path + str(idx) + '.jpg') # 파일 순차적으로 저장
