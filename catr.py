from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

for i in range(1, 5):
    medical_model = load_model('model_final.hdf5')

    image_size = 224

    img_path = f'imgs/img{i}.png'

    img = Image.open(img_path)
    img = img.resize((image_size, image_size))
    
    # Convert image to RGB format
    img = img.convert('RGB')

    x = np.array([np.array(img)])

    plt.figure(figsize=(12, 7))

    prediction = medical_model.predict(x)

    plt.imshow(img)
    plt.xlabel('Prediction: {}'.format(prediction))
    plt.show()
    
    if prediction == 1:
        print("Cataract")
    else:
        print("No Cataract")
