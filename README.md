# 'Rock-Paper-Scissors' Interative Game (Computer Vision)

This project will leverage [Teachable-Machine](https://teachablemachine.withgoogle.com/) to create an interactive version of the classic 'Rock-Paper-Scissors' game. The game will allow the user to play against the computer using their own camera.

## Milestone 1: Set up environment

- Cloned AiCore computer-vision-rock-paper-scissors repo and set up local environment for development.

## Milestone 2: Created Teachable-Machine model
- Using Teachable-Machine, created an image model with 4 classes: 'Rock', 'Paper', Scissors' and 'Nothing' (denoting none of the previous).
- Trained model on 754 images (captured via my own webcam) for each class so model can eventually properly categorise gestures from data provided during game.
- Downloaded tensorflow file and associated labels text file to local machine.
- Pushed aforementioned files to repo.

## Milestone 3: Installed dependencies
- Created a conda environment for game and installed opencv-python, ipykernel and tensorflow accordingly.
- Created requirements.txt pip shortcut for installation of dependencies and pushed file to repo.
- Succcessfully ran Teachable-Machine model locally.

## Milestone 4: Create a Rock-Paper-Scissors game

- Created manual RPS game using Python.
- Abstracted game logic into 4 functions:
  - **get_computer_choice()**: Used choice() from random module to generate computer choice and placed options in tuple as mutability not required. If 'options' variable had required indexing and wider use, may have considered 'namedtuple' for improved readability.

  ```
  get_computer_choice():
    options = ('Rock', 'Paper', 'Scissors')
    computer_choice = random.choice(options)
    return computer_choice
  ```
  - **get_user_choice()**: Used built-in function 'input' to get and return user choice as string.

  ```
  def get_user_choice():
    user_choice = input("Please enter 'Rock', 'Paper' or 'Scissors' to play: ")
    return user_choice
  ```
  - **get_winner()**: Used simple 'if-else' logic to capture all win/loss scenarios and print relevant outcome of game to user. 

  ```
  def get_winner(computer_choice, user_choice):
    if computer_choice == 'Rock' and user_choice == 'Scissors':
        print('You lost')
    elif computer_choice == 'Paper' and user_choice == 'Rock':
        print('You lost')     
    elif computer_choice == 'Scissors' and user_choice == 'Paper':
        print('You lost')
    elif computer_choice == user_choice:
        print('It is a tie!')
    else:
        print('You won!')
  ```
  - **play()**: Called get_winner with get_computer_choice() and get_user_choice passed as arguments to start game and pass required data to 'if-else' logic.

  ```
  def play():
    get_winner(get_computer_choice(), get_user_choice())
  ```

  ## Milestone 5: Use the camera to play Rock-Paper-Scissors

  - Replaced hard-coded user imput with input from user's camera using Teachable-Machine model to predict gesture.
  - Introduced countdown from 3 to 0 before each round played.
  - Threaded function relating to video input so ran in background and wasn't affected by concurrent operations.
  - Implemented a game completion condition wherein the game finishes as soon as either the computer or user reach 3 wins.
  - The following shows a screenshot of the game in action with the output in the terminal.
  ![rps_screenshot_1](https://user-images.githubusercontent.com/126958930/223478191-251c8ad5-dc93-456d-8615-21bcfed441d1.jpg)
  - Intend to refactor code, including use of class-based structure. Could also change the countdown to appear as text in the video interface.





