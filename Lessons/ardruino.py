from pyfirmata import Arduino
import pyfirmata
import time


board = Arduino('COM5')
print("Communication Successfully started")

data = pyfirmata.util.Iterator(board)
data.start()

def flash_LED(board):
    LED_12 = board.digital[3]
    LED_12.mode = pyfirmata.OUTPUT
    LED_12.write(0)

    for _ in range(3):
        LED_12.write(1)
        time.sleep(0.5)
        LED_12.write(0)
        time.sleep(0.5)

#flash_LED(board)

def button_led(board):
    button = board.digital[4]
    button.mode = pyfirmata.INPUT
    LED_3 = board.digital[3]
    LED_3.mode = pyfirmata.OUTPUT
    LED_3.write(0)

    while True:
        button_state = button.read()
        print(button_state)
        if button_state == 1:
            LED_3.write(1)
        else:
            LED_3.write(0)
#button_led(board)

def binary_led_counting(board):
    LED_1 = board.digital[3]
    LED_2 = board.digital[4]
    LED_3 = board.digital[5]

    A = 4*[False] + 4*[True]
    B = 2*[False,False,True,True]
    C = 4*[False, True]

    for n in range(len(A)):
        LED_1.write(int(A[n]))
        LED_2.write(int(B[n]))
        LED_3.write(int(C[n]))
        time.sleep(0.5)

def yn_button(board, anwer):
    Ybutton = board.digital[4]
    Ybutton.mode = pyfirmata.INPUT
    Nbutton = board.digital[9]
    Nbutton.mode = pyfirmata.INPUT
    LED_3 = board.digital[3]
    LED_3.mode = pyfirmata.OUTPUT
    LED_3.write(0)

    while True:
        Ybutton_state = Ybutton.read()
        Nbutton_state = Nbutton.read()
        if Ybutton_state == 1 and anwer == True:
            LED_3.write(1)
            break
        elif Nbutton_state == 1 and anwer == False:
            LED_3.write(1)
            break
        elif Ybutton_state == 1 or Nbutton_state == 1:
            break
    time.sleep(3)
    LED_3.write(0)

def validate_questions(board):
    game = {"is a sky blue?": "Y", "is a sky green?": "N", "is a sky red?": "N"}

    for question in game:
        print(question)
        valid = False
        
        correct = game[question]
        yn_button(board, correct)

            
            
validate_questions(board)

        
board.exit()