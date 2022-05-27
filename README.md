# SIT319-Assignment2
SIT319-Assignment2

Python Flask was used to create a front-end web application that uses the flask, keras, numpy, tensorflow, and pillow packages. Users can upload any photo they choose to the online app. Two Python scripts were written to render the image from the upload form and feed it into ourthe waste classification model. A a function was defined that calls the model prediction for each uploaded image. These scripts were linked to an html page to output an image classification: "Organic" or "Recycled," as well as a likelihood score.

To set up our Flask App, the procedures outlined in the following article was followed:

Link: https://medium.com/@arifulislam_ron/flask-web-application-to-classify-image-using-vgg16-d9c46f29c4cd
Author: Arif Ul Islam (Ron)

# File Structure:
```
Project
│   index.py
│   main.py 
│
└───Resources
│   │    
│   └───Model
│     	  cnn.hdf5
│  
└───Templates
│   	  index.html
│          
└───static (uploaded images will be stored here) -- must be named "static"
```       
Note: Within the index.py and main.py files, you may need to change some file paths to match your system path structure. Within the main.py file, change the paths for line 14 and 15. Within the index.py file, change the paths for lines 14 and 41.

# How to run this app locally:

Setup/Requirements:
1) Visual Studio Code (suggested)
2) Chrome browser (recommended)
3) Python (required)
4) See the dependencies, which may require installation

# Steps:

1) Download files into the above file structure
2) Change file paths per above instructions
3) Open and run the index.py file in the terminal
4) Once run, a web address will appear at the bottom of the terminal.
5) Open brower at "localhost:5000".
6) Select an image file using the "Choose File" button then click on "Submit".
7) This should return a classification and probability score.
