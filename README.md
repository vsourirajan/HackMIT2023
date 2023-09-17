# HackMIT 2023

Project Title: CaptionsToLife <br />
Members: Vaibhav Sourirajan (Table 47) <br />

Description: This project uses an encoder-decoder architecture to caption images, which are then output as audio. We used a ResNet50 model to create image encodings and an LSTM to predict words of the caption from the image and the already partially-generated sequence. We use Flask to create the web app.

Check out a demo here: 

How to run the web app: 
- Clone the repo
- Install the requirements with `pip install -r requirements.txt`
- Run the web app using the following command: `python -m flask run`