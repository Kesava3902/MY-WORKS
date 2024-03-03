# Deeplearning algorithm RNN(recurrent neural network)
# Building an chatbot equipped with sentiment analysis capabilities using NLP techniques
# to classify user message as positive,negative or neutral

# sentiment analysis of user about movie reviews
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

max_features = 10000 # Maximum number of words to include in the vocabulary
max_length= 100 # Maximum length of each review (in words)

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)

# Pad sequences to have equal length:
X_train =sequence.pad_sequences (X_train, maxlen=max_length)
X_test =sequence.pad_sequences ( X_test, maxlen=max_length)

# Build the sentiment analysis model
embedding_dim= 100 # Dimensionality of word embeddings
hidden_units= 64 # Number of LSIM units

# Creating a simple RNN model
model = Sequential()
model.add(Embedding (input_dim=max_features, output_dim=embedding_dim, input_length=max_length))
model.add(LSTM(hidden_units))
model.add(Dense(1,activation = "sigmoid"))
model.compile(loss='binary_crossentropy',optimizer ="adam",metrics=["accuracy"])
model.fit(X_train,y_train,batch_size=32,epochs=5,validation_data=(X_test,y_test))

def predict_sentiment (model, text):
  # Preprocess the input text
  word_to_index = imdb.get_word_index()
  words = text.lower().split()
  encoded_text = [word_to_index[word] + 3 for word in words if word in word_to_index]
  print (encoded_text)
  # Pad the sequence
  sequen = sequence.pad_sequences([encoded_text], maxlen=max_length)
  # Predict the sentiment
  prediction = model.predict(sequen)[0][0]
  sentiment =  'neutral' if prediction == 0.5 else ('negative' if prediction <0.5 else 'positive')
  return sentiment

#Take user input and predict sentiment
while True:
  try:
    user_input = input("Enter a text for sentiment analysis: ")
    if user_input == "stop":
      break
    result = predict_sentiment (model, user_input)
    print("Sentiment:", result)
  except Exception as e:
    print(e)