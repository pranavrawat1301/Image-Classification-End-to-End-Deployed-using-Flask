# Image-Classification-End-to-End-Deployed-using-Flask
This GitHub repository hosts an image classification project deploying a Convolutional Neural Network (CNN) with Flask. Users can upload images through a web interface, receiving real-time predictions on whether the image contains a cat or a dog. The project features a user-friendly interface, model persistence, and easy integration.


*An .ipynb notebook is also provided along with .py files for quick kaggle or jupyter implementation without the use of Flask.*


## Overview

This GitHub repository contains an end-to-end project for image classification using a Convolutional Neural Network (CNN). The CNN model is built using Keras and trained on a dataset containing images of cats and dogs. The trained model is then deployed using Flask, allowing users to upload an image through a web interface and receive real-time predictions on whether the uploaded image is of a cat or a dog.

## Project Structure

- **cnn_complete.py**: Python script containing the code for building, training, and saving the CNN model.
  
- **main.py**: Flask application script responsible for handling user requests, image uploads, and making predictions using the trained model.

- **templates/index.html**: HTML template for the main page where users can upload images.

- **templates/result.html**: HTML template for the result page displaying the prediction and the uploaded image.

- **static/css/style.css**: CSS stylesheet for styling the HTML templates.

- **uploads**: Folder to store temporarily uploaded images.

## Getting Started

1. Clone the repository: `git clone https://github.com/your_username/image-classification-flask.git`

2. Install the required dependencies: `pip install -r requirements.txt`

3. Run the Flask application: `python main.py`

4. Open your browser and go to `http://127.0.0.1:5000/` to use the image classification web application.

## Features

- **Image Upload**: Users can upload images through a user-friendly web interface.

- **Real-time Prediction**: The deployed model provides real-time predictions on whether the uploaded image contains a cat or a dog.

- **Model Persistence**: The trained CNN model is saved in an h5 file, enabling easy loading and reuse.

## Dependencies

- Flask
- Keras
- NumPy
- TensorFlow


Feel free to contribute, report issues, or suggest improvements to make this project even better!
