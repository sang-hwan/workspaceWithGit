import cv2
import os

# filepath 지정하고 파일을 video 변수에 저장
filepath = './ComputerVision/house_zip_3/toilet.mp4'
video = cv2.VideoCapture(filepath)

# video 변수에 파일이 잘 저장되어 있는지 확인
if not video.isOpened():
    print("Could not Open :", filepath)
    exit(0)

# video의 length, width, height, 그리고 fps를 확인
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv2.CAP_PROP_FPS)

print("length :", length)
print("width :", width)
print("height :", height)
print("fps :", fps)

print("video.get(1): ", video.get(1))

# video를 프레임 단위로 처리한 뒤 저장할 directory를 생성
try:
    if not os.path.exists(filepath[:-4]):
        os.makedirs(filepath[:-4])
except OSError:
    print ('Error: Creating directory. ' +  filepath[:-4])

# video를 프레임 단위로 처리
count = 0

while(video.isOpened()):
    ret, image = video.read()
    if(int(video.get(1)) % 30 == 0): # 앞서 불러온 fps 값을 사용하여 1초마다 추출
        cv2.imwrite(filepath[:-4] + "/frame%05d.jpg" %count, image)
        print('Saved frame number :', str(int(video.get(1))))
        count += 1
        
video.release()