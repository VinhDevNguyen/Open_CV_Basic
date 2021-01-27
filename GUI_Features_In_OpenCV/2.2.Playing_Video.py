# Playing video from file
import cv2 as cv

cap = cv.VideoCapture("./Video/Demo.mkv")

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly net is True
    if not ret:
        print("Can't recive frame. Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the result frame
    cv.imshow('Gray Frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# When everthing done, release the capture
cap.release()
cv.destroyAllWindows()
