from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def predict_image_class(image_path, model_path="keras_Model.h5", labels_path="labels.txt"):
    # Load the model
    model = load_model(model_path, compile=False)

    # Load the labels
    class_names = open(labels_path, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Open and preprocess the image
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predict the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name[2:], confidence_score

# Örnek kullanım:
#image_path = "<IMAGE_PATH>"
#class_name, confidence_score = predict_image_class(image_path)
#print("Class:", class_name)
#print("Confidence Score:", confidence_score)
