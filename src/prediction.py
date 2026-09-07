import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tensorflow.keras.models import load_model


# Load the trained model
MODEL_PATH = "handwritten_character_recognition.keras"
model = load_model(MODEL_PATH)


def predict_digit(image_path):
    """
    Predict the handwritten digit in an image.

    Parameters:
        image_path (str): Path to the input image.

    Returns:
        predicted_digit (int): Predicted digit from 0 to 9.
        confidence (float): Prediction confidence as a percentage.
    """

    # Open image and convert to grayscale
    image = Image.open(image_path).convert("L")

    # Resize image to MNIST dimensions
    image = image.resize((28, 28))

    # Convert image to NumPy array
    image_array = np.array(image, dtype="float32")

    # Invert image if the background is bright
    if image_array.mean() > 127:
        image_array = 255.0 - image_array

    # Normalize pixel values
    image_array = image_array / 255.0

    # Reshape for CNN input
    input_image = image_array.reshape(1, 28, 28, 1)

    # Make prediction
    probabilities = model.predict(input_image, verbose=0)[0]

    # Get predicted digit
    predicted_digit = int(np.argmax(probabilities))

    # Get confidence
    confidence = float(np.max(probabilities) * 100)

    # Display image and prediction
    plt.figure(figsize=(4, 4))
    plt.imshow(image_array, cmap="gray")
    plt.title(
        f"Predicted Digit: {predicted_digit}\n"
        f"Confidence: {confidence:.2f}%"
    )
    plt.axis("off")
    plt.show()

    return predicted_digit, confidence


if __name__ == "__main__":
    image_path = input("Enter the path of the handwritten digit image: ")

    try:
        digit, confidence = predict_digit(image_path)

        print("\n========== Prediction Result ==========")
        print(f"Predicted Digit : {digit}")
        print(f"Confidence      : {confidence:.2f}%")

    except FileNotFoundError:
        print("Error: Image file not found. Please check the image path.")

    except Exception as error:
        print(f"Error while processing the image: {error}")
