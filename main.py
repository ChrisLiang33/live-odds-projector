import cv2

stream_link = "path_to_video_or_stream"
cap = cv2.VideoCapture(stream_link)

if not cap.isOpened():
    print("Error: Could not open video stream or file")
    exit(1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('stream ended')
        break
    cv2.imshow('ufc stream', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()