import cv2
from keras.models import load_model
import numpy as np
import time
from threading import Thread, Event
from random import choice

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)       
vid_input = False
options = ('Rock', 'Paper', 'Scissors','Nothing')
computer_wins = 0
user_wins = 0

def countdown(seconds):
  for countdown in range(seconds,0,-1):
     print(f'{countdown}...')
     time.sleep(1)

def get_user_input(event):    
    global vid_input, cap
    while True:
      ret, frame = cap.read()
      resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
      image_np = np.array(resized_frame)
      normalized_image = (image_np.astype(np.float32) / 127.0) - 1
      data[0] = normalized_image
      cv2.imshow('frame', frame)
      vid_input = True
      if cv2.waitKey(1) & 0xFF == ord('q'):
         break
      if event.is_set():
         break
      
def get_prediction(data):
   predictions_arr = model.predict(data)
   prediction = options[int(predictions_arr.argmax(axis=1))]
   print(f'Your choice: {prediction}')
   return prediction

def get_computer_choice():
   computer_choice = choice(options[:3])
   print(f'Computer choice: {computer_choice}')
   return computer_choice

def get_round_winner(user_choice, computer_choice):
    global computer_wins, user_wins    
    
    loss_scenarios = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
    if user_choice == 'Nothing':
       print('You didn\'t make a choice. Try again.') 
    elif loss_scenarios[computer_choice] == user_choice:
       print('You lost the round')
       computer_wins += 1
    elif computer_choice == user_choice:
       print('It is a tie!')
    else:
       print('You won the round!')
       user_wins += 1

def play():
  event = Event()
  thread = Thread(target=get_user_input, args=(event,))
  thread.start()
  while not vid_input: pass
  while True:
    countdown(3)
    get_round_winner(get_prediction(data), get_computer_choice())
    if computer_wins == 3:
       print('Game over... the computer won.')
       event.set()
       break
    if user_wins == 3:
       print('You won the game!!!')
       event.set()
       break
  
play()