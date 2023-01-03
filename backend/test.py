import cv2

def processVideoStream():
    """Opens a video stream and converts each frame to numpy array."""
    # Open a video stream
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Process the frame
        frame = processImage(frame)

        # Display the frame
        cv2.imshow("frame", frame)

        # Wait for a key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video stream
    cap.release()
    cv2.destroyAllWindows()

def processImage(frame):
    """Takes a numpy image array, resizes the image to 224x224 and returns the resized frame."""
    # Resize the image
    frame = cv2.resize(frame, (224, 224))

    # Get current time in seconds
    time = cv2.getTickCount() / cv2.getTickFrequency()

    # Insert time into the image
    frame = insertText(frame, str(time))

    # Return the resized frame
    return frame

def insertText(frame, text):
    """Takes a numpy image array and a text string and inserts the text into the image."""
    # Insert the text into the image
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Return the image
    return frame

def main():
    processVideoStream()


if __name__ == "__main__":
    main()
