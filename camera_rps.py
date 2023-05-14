import cv2
from keras.models import load_model
import numpy as np
from time import sleep
from threading import Thread, Event
from random import choice 

class Camera_RPS:
   MODEL = load_model('keras_model.h5')
   OPTIONS = ('Rock', 'Paper', 'Scissors','Nothing')
   
   def __init__(self, num_rounds=3, countdown_time=3):
      self.num_rounds = num_rounds
      self.countdown_time = countdown_time
      self.vid_input = False
      self.computer_wins, self.user_wins = 0, 0 
      self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) 
      self.cap = cv2.VideoCapture(0)  
      self.frame = None

   def play(self):
      event = Event()
      thread = Thread(target=self.get_user_input, args=(event,))
      thread.start()
      while not self.vid_input: pass
      while True:
         self.get_countdown(self.countdown_time)
         self.get_round_winner(self.get_computer_choice(), self.get_prediction(self.data))
         game_over_scenarios = {self.computer_wins: 'Game over... the computer won.',
                                self.user_wins: 'Congratulations... you won the game!'}
         game_over_message = game_over_scenarios.get(self.num_rounds)
         if game_over_message:
            print(game_over_message)
            event.set()
            break

   def get_countdown(self, countdown_time):
      for countdown in range(countdown_time,0,-1):
         print(f'{countdown}...')
         sleep(1)

   def get_user_input(self, event):    
      while True:
         ret, frame = self.cap.read()
         resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
         image_np = np.array(resized_frame)
         normalized_image = (image_np.astype(np.float32) / 127.0) - 1
         self.data[0] = normalized_image      
         cv2.imshow('frame', frame)
         self.vid_input = True
         if cv2.waitKey(1) & 0xFF == ord('q'):
            break
         if event.is_set():
            break
         
   def get_prediction(self, data):
      predictions_arr = Camera_RPS.MODEL.predict(data)
      prediction = Camera_RPS.OPTIONS[int(predictions_arr.argmax(axis=1))]
      print(f'Your choice: {prediction}')
      return prediction

   def get_computer_choice(self):
      computer_choice = choice(Camera_RPS.OPTIONS[:3])
      print(f'Computer choice: {computer_choice}')
      return computer_choice

   def get_round_winner(self, computer_choice, user_choice):      
      loss_scenarios = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
      if user_choice == 'Nothing':
         print('You didn\'t make a choice. Try again.') 
      elif loss_scenarios[computer_choice] == user_choice:
         print('You lost the round')
         self.computer_wins += 1
      elif computer_choice == user_choice:
         print('It is a tie!')
      else:
         print('You won the round!')
         self.user_wins += 1

game1 = Camera_RPS(num_rounds=3)
game1.play()