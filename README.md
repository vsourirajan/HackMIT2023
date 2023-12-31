# HackMIT 2023

Project Title: CaptionsToLife <br />
Members: Vaibhav Sourirajan (Table 47) <br />

Description: This project uses an encoder-decoder architecture to caption images, which are then output as audio. We used a ResNet50 model to create image encodings and an LSTM to predict words of the caption from the image and the already partially-generated sequence. We use Flask to create the web app.

Architecture:

<img width="1048" alt="architecture" src="https://github.com/vsourirajan/HackMIT2023/assets/113937608/076f4705-7907-43c0-a6c0-b59f9aa55dac">

Check out a quick demo here: https://youtu.be/-Xexk2l7muQ

How to run the web app: 
- Clone the repo
- Install the requirements with `pip install -r requirements.txt`
- Run the web app using the following command: `python -m flask run`
