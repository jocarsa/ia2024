import cv2
import mediapipe as mp
import threading
import time

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

haypersona = False
stop_thread = False

def capture_video():
    global haypersona
    video_capture = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
        while not stop_thread:
            ret, frame = video_capture.read()
            if not ret:
                continue
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(rgb_frame)
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(frame, detection)
            cv2.imshow('Video', frame)
            if results.detections:
                #print(f"Detected {len(results.detections)} face(s)")
                haypersona = True
            else:
                haypersona = False
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    video_capture.release()
    cv2.destroyAllWindows()

stop_thread = False
video_thread = threading.Thread(target=capture_video)

video_thread.start()

print("The video capture is running in a separate thread.")

try:
    while not stop_thread:
        print("Main thread is running.")
        time.sleep(1)  # Sleep for 1 second
except KeyboardInterrupt:
    stop_thread = True
    video_thread.join()
    print("Video capture stopped.")
