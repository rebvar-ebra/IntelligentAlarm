import cv2
import datetime
import time
import playsound

def main():
    wake_up_time = set_alarm_time("07:00")  # Set your wake-up time here
    bed_area = define_bed_area()  # Define the bed area coordinates
    capture_and_process_video(wake_up_time, bed_area)

def set_alarm_time(alarm_time_str):
    """ Set the alarm time """
    hour, minute = map(int, alarm_time_str.split(":"))
    return datetime.time(hour, minute)

def define_bed_area():
    """ Define the bed area coordinates """
    # This could be a predefined area or you could implement a way for users to select an area in the video feed
    return (x1, y1, x2, y2)

def capture_and_process_video(wake_up_time, bed_area):
    """ Capture video and process frames """
    cap = cv2.VideoCapture(0)  # Initialize the webcam
    reference_frame = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = preprocess_frame(frame)
        if reference_frame is None:
            reference_frame = gray_frame
            continue

        motion_detected = detect_motion(gray_frame, reference_frame, bed_area)
        if is_wake_up_time(wake_up_time) and motion_detected:
            playsound.playsound('alarm_sound.mp3')  # Play the alarm sound
            break

        reference_frame = gray_frame  # Update the reference frame
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def preprocess_frame(frame):
    """ Convert frame to grayscale and apply Gaussian blur """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    return gray

def detect_motion(current_frame, reference_frame, bed_area):
    """ Detect motion in the bed area """
    delta_frame = cv2.absdiff(reference_frame, current_frame)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Check for motion within the bed area
    x1, y1, x2, y2 = bed_area
    motion_area = thresh_frame[y1:y2, x1:x2]
    motion = cv2.countNonZero(motion_area)
    return motion > motion_threshold  # Define a suitable threshold

def is_wake_up_time(wake_up_time):

    current_time = datetime.datetime.now().time()
    return current_time >= wake_up_time

if __name__ == "__main__":
    main()
