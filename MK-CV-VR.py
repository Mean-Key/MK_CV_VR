import cv2

# Video Capture 설정
cap = cv2.VideoCapture(0)  # 0번 카메라 사용

# 사용 가능한 비디오 코덱 및 확장자 목록 설정
fourcc_dict = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),  # AVI 형식의 코덱 설정
    'mov': cv2.VideoWriter_fourcc(*'MJPG'),  # MOV 형식의 코덱 설정
    'mp4': cv2.VideoWriter_fourcc(*'MP4V')   # MP4 형식의 코덱 설정
}
ext_list = list(fourcc_dict.keys())  # 확장자 리스트 생성
current_ext_index = 0  # 현재 확장자 인덱스

# 비디오 속성 설정
fps = 20.0  # 초당 프레임 수
frame_size = (int(cap.get(3)), int(cap.get(4)))  # 프레임 크기 가져오기
out = None  # VideoWriter 객체 초기화

recording = False  # 녹화 상태 변수

while cap.isOpened():
    ret, frame = cap.read()  # 카메라에서 프레임 읽기
    if not ret:
        break

    if recording:
        if out is None:
            current_ext = ext_list[current_ext_index]  # 현재 선택된 확장자
            fourcc = fourcc_dict[current_ext]  # 해당 확장자의 코덱
            out = cv2.VideoWriter(f'output.{current_ext}', fourcc, fps, frame_size)  # 비디오 파일 생성
        out.write(frame)  # 프레임 저장
        cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)  # 화면 왼쪽 상단에 녹화 표시 (빨간 원)
    
    # 현재 저장 확장자 표시 (노란색 텍스트)
    cv2.putText(frame, f'.{ext_list[current_ext_index]}', (70, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    
    cv2.imshow('Video Recorder', frame)  # 프레임 화면 출력
    
    key = cv2.waitKey(1) & 0xFF  # 키 입력 받기
    if key == 27:  # ESC 키 입력 시 종료
        break
    elif key == 32:  # Space 키 입력 시 녹화 시작/중지
        recording = not recording
        if not recording and out is not None:
            out.release()
            out = None
    elif key == ord('f'):  # 'F' 키 입력 시 저장할 동영상 파일 확장자 변경
        current_ext_index = (current_ext_index + 1) % len(ext_list)  # 확장자 변경
        print(f"저장 형식 변경: {ext_list[current_ext_index]}")

cap.release()  # 카메라 해제
if out is not None:
    out.release()  # 비디오 저장 객체 해제
cv2.destroyAllWindows()  # 모든 OpenCV 창 닫기