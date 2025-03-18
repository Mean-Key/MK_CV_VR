# MK's Video Recorder 

## 📌 개요
이 프로그램은 OpenCV를 사용하여 컴퓨터의 웹캠 영상을 녹화하는 Video Recorder입니다.   
이용자는 녹화 시작/중지, 저장 확장자 변경 등의 기능을 키보드 입력을 통해 조작할 수 있습니다.

## 🎥 기능 소개
- ✅ **실시간 웹캠 영상 출력**: 화면에 현재 카메라 영상을 표시합니다.
```python
cap = cv2.VideoCapture(0)  # 0번 카메라 사용
```
- ✅ **녹화 기능**: `Space` 키를 눌러 녹화를 시작/중지할 수 있습니다.
```python
out = cv2.VideoWriter(f'output.{current_ext}', fourcc, fps, frame_size)  # 비디오 파일 생성
```
```python
elif key == 32:  # Space 키 입력 시 녹화 시작/중지
        recording = not recording
        if not recording and out is not None:
            out.release()
            out = None
```
- ✅ **녹화 중 표시 기능**: 화면 좌측 상단에 **🔴 빨간 원**으로 녹화 상태를 표시합니다.
```python
cv2.circle(frame, (50, 50), 10, (0, 0, 255), -1)  # 화면 왼쪽 상단에 녹화 표시 (빨간 원)
```
- ✅ **파일 확장자 변경**: `F` 키를 눌러 저장할 동영상 파일의 확장자를 변경할 수 있습니다. (`.avi`, `.mov`, `.mp4`)
```python
 elif key == ord('f'):  # 'F' 키 입력 시 저장할 동영상 파일 확장자 변경
        current_ext_index = (current_ext_index + 1) % len(ext_list)  # 확장자 변경
```
- ✅ **프로그램 종료**: `ESC` 키를 눌러 프로그램을 종료할 수 있습니다.
```python
if key == 27:  # ESC 키 입력 시 종료
        break
```
## 🖥️ 사용 방법
1. 프로그램 실행 후, 웹캠 영상이 화면에 표시됩니다.
2. `Space` 키를 누르면 **녹화를 시작**합니다. 다시 누르면 **녹화를 중지**합니다.
3. `F` 키를 누르면 저장할 **파일 확장자**가 변경됩니다.
4. `ESC` 키를 누르면 프로그램이 **종료**됩니다.

## 🔄 추가 기능 - 저장 형식 변경
- `F` 키를 누를 때마다 `.avi` → `.mov` → `.mp4` 순서로 변경됩니다.
```python
# 사용 가능한 비디오 코덱 및 확장자 목록 설정
fourcc_dict = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),  # AVI 형식의 코덱 설정
    'mov': cv2.VideoWriter_fourcc(*'MJPG'),  # MOV 형식의 코덱 설정
    'mp4': cv2.VideoWriter_fourcc(*'MP4V')   # MP4 형식의 코덱 설정
}
```
- 현재 선택된 확장자는 화면 좌측 상단에 <mark>노란색</mark>으로 표시됩니다.
```python
# 현재 저장 확장자 표시 (노란색 텍스트)
    cv2.putText(frame, f'.{ext_list[current_ext_index]}', (70, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
```

## 📸 실행 화면
- 프로그램 시작 화면 (동영상 파일의 확장자 표시)   
<img src="https://github.com/Mean-Key/MK_CV_VR/blob/main/screenshot/start.png" width="600" height="400"/>   

- 녹화 시작 화면 (**🔴 빨간 원** 표시)   
<img src="https://github.com/Mean-Key/MK_CV_VR/blob/main/screenshot/recode-avi.png" width="600" height="400"/>   

- 파일 확장자 변경 화면 (`.avi` &rarr; `.mov`)   
<img src="https://github.com/Mean-Key/MK_CV_VR/blob/main/screenshot/recode-mov.png" width="600" height="400"/>   

- 파일 확장자 변경 화면 (`.mov` &rarr; `.avi`)   
<img src="https://github.com/Mean-Key/MK_CV_VR/blob/main/screenshot/recode-mp4.png" width="600" height="400"/>   

- 웹캠 녹화 화면 (README.md에 업로드를 위해 `gif`로 변환, **🔴 빨간 원**, **파일 확장자** 표시 :negative_squared_cross_mark:)
<img width="80%" src="https://github.com/Mean-Key/MK_CV_VR/blob/main/video/output.gif"/>

