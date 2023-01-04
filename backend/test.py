import cv2
import torch

def processVideoStream(device, model):
    """Opens a video stream and converts each frame to numpy array."""
    # Open a video stream
    cap = cv2.VideoCapture(0)


    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Process the frame
        frame = processImage(frame, device, model)

        # Display the frame
        cv2.imshow("frame", frame)

        # Wait for a key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video stream
    cap.release()
    cv2.destroyAllWindows()

def processImage(frame, device, model):
    """Takes a numpy image array, resizes the image to 420x420 and returns the resized frame."""
    # Resize the image
    frame = cv2.resize(frame, (420, 420))

    # Create a torch float tensor from the frame and move it to the device
    frameTensor = torch.from_numpy(frame).float().to(device)

    # Reshape the tensor to 1x3x420x420
    frameTensor = frameTensor.reshape(1, 3, 420, 420)
    # Use the model to make a prediction
    with torch.no_grad():
        prediction = model(frameTensor).detach().cpu()

    # Get the top prediction and its index
    topPrediction, topIndex = torch.topk(prediction, 1)

    # Insrt the top prediction and its index into the frame
    frame = insertText(frame, f"Prediction: {topPrediction.item()} Index: {topIndex.item()}")

    # Return the processed frame
    return frame

def insertText(frame, text):
    """Takes a numpy image array and a text string and inserts the text into the image."""
    # Insert the text with white font of size 8 into the image
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 255), 2)
    
    # Return the image
    return frame


def checkTorchMPSBackend():
    """Checks if the torch MPS backend is available."""
    # Check if the MPS backend is available
    if torch.backends.mps.is_available():
        print("Torch MPS backend is available.")
        return True
    else:
        print("Torch MPS backend is not available.")
        return False

def loadResnet50Model(device):
    """Loads the Resnet50 model and moves it to the device."""
    # Load the Resnet50 model
    model = torch.hub.load("pytorch/vision:v0.6.0", "resnet50", pretrained=True)

    # Move the model to the device
    model.to(device)

    # Return the model
    return model

def main():
    # Set device to MPS if available, else set to CPU
    if checkTorchMPSBackend():
        device = torch.device("mps")
    else:
        device = torch.device("cpu")
    
    # Load the Resnet50 model
    model = loadResnet50Model(device)

    processVideoStream(device, model)


if __name__ == "__main__":
    main()
