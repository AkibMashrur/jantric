
def processVideoStream():
    """Opens a video stream and converts each frame to black and white."""
    import cv2

    # Open a video stream
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Convert the frame to black and white
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the frame
        cv2.imshow("frame", gray)

        # Wait for a key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video stream
    cap.release()
    cv2.destroyAllWindows()

def main():
    processVideoStream()


if __name__ == "__main__":
    main()
