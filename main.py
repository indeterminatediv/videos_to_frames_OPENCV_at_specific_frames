import cv2
import os
from PIL import Image

cap = cv2.VideoCapture('video file name/path')
frame_rate = cap.get(cv2.CAP_PROP_FPS)
print(frame_rate)
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(total_frames)
num_frames_to_extract = 20
interval = int(total_frames / num_frames_to_extract)
save_dir = 'frames'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

frame_counter = 66710
i = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if frame_counter % interval == 0:
        save_path = os.path.join(save_dir, f'{frame_counter:04d}.jpg')
        cv2.imwrite(save_path, frame)
    frame_counter += 1
    i = i + 1
    if frame_counter >= total_frames:
        break

# cap.release()
