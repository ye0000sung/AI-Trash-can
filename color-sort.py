import cv2
import numpy as np
import serial
import time

# 시리얼 통신 객체 생성 
ser = serial.Serial('COM7',9600)

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# HSV 색상 범위 정의
colors = {
    'red': ((0, 100, 100), (10, 255, 255)),
    'green': ((50, 100, 100), (70, 255, 255)),
    'blue': ((110, 100, 100), (130, 255, 255))
}

# 색상 이름 정의
color_names = {
    'red': 'Red',
    'green': 'Green',
    'blue': 'Blue'
}

# 색상에 따른 분류 영역 정의
positions = {
    'red': 0,
    'green': 1,
    'blue': 2
}

# 화면 크기 가져오기
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 폰트 및 색상 설정
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
thickness = 2
text_color = (255, 255, 255)

# 무한 루프
while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 색공간 변환 (BGR -> HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 색상 별 마스크 생성
    masks = {}
    for color, (lower, upper) in colors.items():
        mask = cv2.inRange(hsv, lower, upper)
        masks[color] = mask

    # 색상 영역 추출
    areas = {}
    for color, mask in masks.items():
        count = cv2.countNonZero(mask)
        if count > 0:
            moments = cv2.moments(mask)
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            areas[color] = (cx, cy, count)

    # 분류 결과 그리기
    img_draw = frame.copy()
    for color, area in areas.items():
        cx, cy, count = area
        cv2.circle(img_draw, (cx, cy), 10, (0, 255, 0), -1)
        position = positions[color]
        cv2.putText(img_draw, color_names[color], (width-200, 50+position*50), font, font_scale, text_color, thickness, cv2.LINE_AA)

    # 비디오 프레임 출력
    cv2.imshow('frame', img_draw)

    # 감지된 색상에 따라 아두이노 시리얼통신

    if 'red' in areas:
     ser.write(b'1')
    elif 'green' in areas:
     ser.write(b'2')
    elif 'blue' in areas:
      ser.write(b'3')


# 비디오 캡처 객체와 윈도우 창 해제
cap.release()
cv2.destroyAllWindows()
