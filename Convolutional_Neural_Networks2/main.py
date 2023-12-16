from flask import Flask, render_template, request
from keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Specify the upload folder

classifier = load_model('cnn.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    
    from keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(rescale = 1./255,
                                       shear_range = 0.2,
                                       zoom_range = 0.2,
                                       horizontal_flip = True)

    
    training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                     target_size = (64, 64),
                                                     batch_size = 32,
                                                     class_mode = 'binary')

    
    if request.method == 'POST':
        file = request.files['file']
        img_path = "uploads/" + file.filename
        file.save(img_path)

        # Load and preprocess the uploaded image
        test_image = image.load_img(img_path, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        # Make a prediction
        result = classifier.predict(test_image)
        class_indices = training_set.class_indices
        
        print(class_indices)
        
        if result[0][0] == 1:
            prediction = 'Dog'
        else:
            prediction = 'Cat'

        # Convert the image to base64 encoding
        with open(img_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode('utf-8')

        return render_template('result.html', encoded_image=encoded_image, prediction=prediction)
if __name__ == '__main__':
    app.run(debug=False)



