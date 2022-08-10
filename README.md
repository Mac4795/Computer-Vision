# Computer Vision - Rock, Paper, Scissors
Rock, paper, scissors using Teachable Machine to collect images to create a model that recognises hand gestures.

## Creating the Model
- First step was to create the image model using Teachable Machine. Using the built in webcam, recording specific hand gestures directly to the website, between 300 - 450 images, infront of a plain backgroud and without my face in the same frame. 
- Creating four different classes for the three specific hand gestures associated with the game and allowing those images to train the machine. This took a couple of minutes. 
- Once the machine has been trained, the model is ready to be previewed and downloaded. 
<img width="1242" alt="Screenshot 2022-08-08 at 8 41 24 pm" src="https://user-images.githubusercontent.com/95615535/183734562-42defd25-96c2-46c0-93ad-97d1cacded8d.png">

## Creating the game
- Once the model has been downloaded to a .h5 file, the game play can be written. 
- Using python to create a simple rock, paper, scissors game where the computers choice is a random guess and you are able to input your guess before the computers guess is revealed. 
``` python 
def play():
    player = get_user_choice()
    computer = get_computer_choice()
    print(get_winner(computer, player))
```
- After testing the game, it was clear that the code was not recognising the user/player input when the first letter of the word was not capitalised.
- A simple adjustment of using the ``` .capitalize() ``` method to ensure that what ever the input from the use is, the first letter will be capitalised. 
