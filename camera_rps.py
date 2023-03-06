import cv2
from keras.models import load_model
import numpy as np
import time
from threading import Thread, Event

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)       
vid_input = False

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
   prediction = model.predict(data)
   options = ('Rock', 'Paper', 'Scissors', 'Nothing')
   print(f'Prediction: {options[int(prediction.argmax(axis=1))]}')

def play():
  event = Event()
  thread = Thread(target=get_user_input, args=(event,))
  thread.start()
  while not vid_input: pass
  for _ in range(3):
    countdown(3)
    get_prediction(data)	
  event.set()

play()