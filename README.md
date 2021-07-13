# AI-Chatbot
AI and NLTK based Personal chatbot

## [Prerequisites](https://github.com/PatelVatsalB21/AI-Chatbot/blob/main/requirements.txt)
- Tensorflow
- Flask
- NLTK
- Gunicorn(For deployment on heroku)

## Installation
Install Tensorflow - `pip install tensorflow`

Install Flask - `pip install flask`

Install Gunicorn - `pip install gunicorn`

Install NLTK - `pip install nltk`

We need two specific libraries **wordnet** and **punkt** from NLTK so open Python terminal and write the following commands:-
`import nltk
nltk.download('wordnet')`
After successfull installation of **wordnet**, install **punkt**.
`nltk.download('punkt')`
 
## Training and Running model 

### Training 
The [trainer.py](https://github.com/PatelVatsalB21/AI-Chatbot/blob/main/trainer.py) file is present in repo. To run the trainer use `python trainer.py`.

Trainer is based on Keras Sequential model with Dense layers and Dropouts to avoid overfitting. The model uses softmax function for the output and SGD optimizer with learning rate `0.01`. Also Keras Callback is used to stop training if loss does not decrease with patience `5`. After training model is save in `.h5` format.

### Running the pretrained model
The [app.py](https://github.com/PatelVatsalB21/AI-Chatbot/blob/main/app.py) file is present in repo. To run the model use `python app.py`.

On running currently the app will be deployed on the localhost and it can be further deployed via any cloud services. The input output of the model can be done with JSON requests. To test the model locally on computer remove Flask entites and use `input()` and `print()` with the `predict()` method.
