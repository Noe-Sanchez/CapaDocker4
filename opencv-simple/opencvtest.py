import time
import cv2

def capture_headless_image(filename="captured_image.jpg"):
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return

    ret, frame = cap.read()
    
    if ret:
        cv2.imwrite(filename, frame)
        print(f"Success: Image saved to {filename}")
    else:
        print("Error: Could not read a frame from the webcam.")
    
    cap.release()

if __name__ == "__main__":
    capture_headless_image()

