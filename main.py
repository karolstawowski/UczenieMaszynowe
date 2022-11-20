import numpy as np
import cv2

capture = cv2.VideoCapture('./assets/input_video.MP4')
video_output = cv2.VideoWriter('./assets/output_video.mp4',
                               cv2.VideoWriter_fourcc(*'mp4v'),
                               30,
                               (1920, 1080))

while True:
    status, frame = capture.read(0)
    if status:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_range = np.array([0, 190, 20])
        upper_range = np.array([160, 255, 255])
        mask = cv2.inRange(image, lower_range, upper_range)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        result[0:370, 0:1920] = [0, 0, 0]
        video_output.write(result)
    else:
        break

capture.release()
video_output.release()
print("File saved")
