from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/catr', methods=['GET', 'POST'])
def catr():
    if request.method == 'POST':
        # Check if the POST request has a file part
        if 'file' not in request.files:
            return render_template('catr.html', message='No file part')
        
        file = request.files['file']
        
        # Check if the file is empty
        if file.filename == '':
            return render_template('catr.html', message='No selected file')
        
        # Process the uploaded file
        # For example, save the file to a desired location
        file.save('imgs/' + file.filename)
        test_img = 'imgs/' + file.filename
      
        medical_model = load_model('model_final.hdf5')

        image_size = 224

            # img_path = f'imgs/img{i}.png'

        img = Image.open(test_img)
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
            msg = "The Person is Having Cataract"
        else:
            msg = "The Person is Not HavingNot Cataract"

        return render_template('catr.html', message=msg)
    
    return render_template('catr.html')


@app.route('/brain')
def brain():
    return render_template('brain.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission logic here
    name = request.form['name']
    # ...

if __name__ == '__main__':
    app.run(debug=True)


