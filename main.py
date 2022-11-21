import numpy as np
import cv2

capture = cv2.VideoCapture('./assets/input_video.MP4')
video_output = cv2.VideoWriter('./assets/output_video.mp4',
                               cv2.VideoWriter_fourcc(*'mp4v'),
                               30,
                               (1920, 1080))

lower_range_lower_red = np.array([0, 100, 50])
upper_range_lower_red = np.array([10, 255, 255])
lower_range_upper_red = np.array([160, 100, 20])
upper_range_upper_red = np.array([179, 255, 255])
lower_range_b = np.array([100, 150, 0])
upper_range_b = np.array([140, 255, 255])

while True:
    status, frame = capture.read(0)
    if status:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red_mask = cv2.inRange(image, lower_range_lower_red, upper_range_lower_red)
        upper_red_mask = cv2.inRange(image, lower_range_upper_red, upper_range_upper_red)
        blue_mask = cv2.inRange(image, lower_range_b, upper_range_b)
        result = cv2.bitwise_and(frame, frame, mask=lower_red_mask + upper_red_mask + blue_mask)
        result[0:370, 0:1920] = [0, 0, 0]
        video_output.write(result)
    else:
        break

capture.release()
video_output.release()
print("File saved")
