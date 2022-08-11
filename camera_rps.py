import cv2
import numpy as np
import random

from keras.models import load_model 

class Computer_vision:

    def __init__(self):
        self.computer_score = 0
        self.player_score = 0 

    def computer_choice():
        choice = ['Rock','Paper','Scissors']
        computer_choice = random.choice(choice)
        return computer_choice

    def get_predictions():
        model = load_model('keras_model.h5')

        capture = cv2.VideoCapture(0)
        info = np.ndarray(shape=(1, 224, 224, 3), dtype = np.float32)
        time = cv2.waitkey(5)

        while time:
            ret, frame = capture.read()
            frame_size = cv2.resize(frame, (222,222), interpolation = cv2.INTER_AREA)
            image = np.array(frame_size)
            norm_image = (image.astype(np.float32) / 127.0) - 1
            info[0] = norm_image

            font = cv2.FONT_HERSHEY_DUPLEX 
            cv2.putText(frame, str(int(cv2.waitkey(5)))),(200, 500), font, 7, (0, 255, 255), 4, cv2.LINE_AA
            
            cv2.imshow('frame', frame)

            if cv2.waitkey(2) == ord('q'):
                break

        predictions = model.predict(info)
        max_index = np.argmax(predictions[0])
        return max_index

    def user_choice(self):
        max_index = self.get_predictions()
        if max_index == 0:
            user_choice = 'Rock'
        elif max_index == 1:
            user_choice = 'Paper'
        elif max_index == 2:
            user_choice = 'Scissors'
        else:
            user_choice = 'Nothing'
        return user_choice

    def winner(self):
        user_select = self.user_choice()
        computer_select = self.computer_choice()

        print(user_select)
        print(computer_select)

        if user_select == 'Rock' and computer_select =='Paper' or user_select == 'Scissors' and computer_select == 'Rock' or user_select == 'Paper' and computer_select == 'Scissors':
            self.computer_score += 1
            return 'The computer won, better luck next time.'
        elif user_select == computer_select:
            return 'Its a tie!'
        else:
            self.player_score += 1
            return 'Congrats! You beat the computer!'

    def play(self):
        while self.computer_score < 3 and self.player_score < 3:
            self.winner()
            print(f'Your score is: {self.player_score} and the computers score is: {self.computer_score}')

        self.capture.release()
        cv2.destroyAllWindows()
        

game = Computer_vision()
game.play()

