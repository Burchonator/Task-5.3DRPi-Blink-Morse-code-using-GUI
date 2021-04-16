import sys
from PyQt5.QtWidgets import *#QApplication,QWidget,QRadioButton
from PyQt5.QtGui import *#QIcon

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

lightpin = 8
GPIO.setup(lightpin,GPIO.OUT) # red
# when output set to high the voltage is 3.3V, 0 for Low
# Never connect a device with an input voltage higher than 3.3V to GPIO pin
# because it will fry the RaspPi

import time

timeunit = 0.3 # means 3 ms

# class for functions that flash signals
class Signals:
    def dot(self):
        signal=Signals
        GPIO.output(lightpin,GPIO.HIGH)
        time.sleep(timeunit)
        signal.space(self)
    def dash(self):
        signal=Signals
        GPIO.output(lightpin,GPIO.HIGH)
        time.sleep(timeunit*3)
        signal.space(self)
    def space(self):
        signal=Signals
        GPIO.output(lightpin,GPIO.LOW)
        time.sleep(timeunit)
    def nextletter(self):
        signal=Signals
        GPIO.output(lightpin,GPIO.LOW)
        time.sleep(timeunit*3)
    def nextword(self):
        signal=Signals
        GPIO.output(lightpin,GPIO.LOW)
        time.sleep(timeunit*6)
        # six time units instead of 7 to compensate the the space in nextletter() in a letter function
    
    def lettera(self):
        signal = Signals
        signal.dot(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterb(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.nextletter(self)
    def letterc(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.dash(self)
        signal.dot(self)
        signal.nextletter(self)
    def letterd(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
        signal.nextletter(self)
    def lettere(self):
        signal = Signals
        signal.dot(self)
        signal.nextletter(self)
    def letterf(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dash(self)
        signal.dot(self)
    def letterg(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dot(self)
        signal.nextletter(self)
    def letterh(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.nextletter(self)
    def letteri(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.nextletter(self)
    def letterj(self):
        signal = Signals
        signal.dot(self)
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterk(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterl(self):
        signal = Signals
        signal.dot(self)
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
        signal.nextletter(self)
    def letterm(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.nextletter(self)
    def lettern(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.nextletter(self)
    def lettero(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterp(self):
        signal = Signals
        signal.dot(self)
        signal.dash(self)
        signal.dash(self)
        signal.dot(self)
        signal.nextletter(self)
    def letterq(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dot(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterr(self):
        signal = Signals
        signal.dot(self)
        signal.dash(self)
        signal.dot(self)
        signal.nextletter(self)
    def letters(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.nextletter(self)
    def lettert(self):
        signal = Signals
        signal.dash(self)
        signal.nextletter(self)
    def letteru(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterv(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterw(self):
        signal = Signals
        signal.dot(self)
        signal.dash(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterx(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
        signal.dash(self)
        signal.nextletter(self)
    def lettery(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.dash(self)
        signal.dash(self)
        signal.nextletter(self)
    def letterz(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
        signal.nextletter(self)
    def number1(self):
        signal = Signals
        signal.dot(self)
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
    def number2(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
    def number3(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dash(self)
        signal.dash(self)
    def number4(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dash(self)
    def number5(self):
        signal = Signals
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
    def number6(self):
        signal = Signals
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
    def number7(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
        signal.dot(self)
    def number8(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.dot(self)
        signal.dot(self)
    def number9(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.dot(self)
    def number0(self):
        signal = Signals
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)
        signal.dash(self)

# class for what is displayed on gui
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Morse Code Blinker'
        self.left = 200 
        self.top = 200
        self.width = 400
        self.height = 300
        rbtnwidth = 70
        rbtnheight = 40
        layout=QGridLayout()

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setGeometry(200,200,400,300)
        
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.textbox.setMaxLength(12)
        
        # Create a button in the window
        self.button = QPushButton('Play Morse Code', self)
        self.button.move(20,80)
        # connect button to function on_click
        self.button.clicked.connect(self.play_morse)
        
        #self.show()
        
    def play_morse(self):
        signal = Signals
        message = str(self.textbox.text()).lower()
        
        for letter in message:
            if letter == 'a':
                signal.lettera(self)
            elif letter == 'b':
                signal.letterb(self)
            elif letter == 'c':
                signal.letterc(self)
            elif letter == 'd':
                signal.letterd(self)
            elif letter == 'e':
                signal.lettere(self)
            elif letter == 'f':
                signal.letterf(self)
            elif letter == 'g':
                signal.letterg(self)
            elif letter == 'h':
                signal.letterh(self)
            elif letter == 'i':
                signal.letteri(self)
            elif letter == 'j':
                signal.letterj(self)
            elif letter == 'k':
                signal.letterk(self)
            elif letter == 'l':
                signal.letterl(self)
            elif letter == 'm':
                signal.letterm(self)
            elif letter == 'n':
                signal.lettern(self)
            elif letter == 'o':
                signal.lettero(self)
            elif letter == 'p':
                signal.letterp(self)
            elif letter == 'q':
                signal.letterq(self)
            elif letter == 'r':
                signal.letterr(self)
            elif letter == 's':
                signal.letters(self)
            elif letter == 't':
                signal.lettert(self)
            elif letter == 'u':
                signal.letteru(self)
            elif letter == 'v':
                signal.letterv(self)
            elif letter == 'w':
                signal.letterw(self)
            elif letter == 'x':
                signal.letterx(self)
            elif letter == 'y':
                signal.lettery(self)
            elif letter == 'z':
                signal.letterz(self)
            elif letter == ' ':
                signal.nextword(self)
            elif letter == '1':
                signal.number1(self)
            elif letter == '2':
                signal.number2(self)
            elif letter == '3':
                signal.number3(self)
            elif letter == '4':
                signal.number4(self)
            elif letter == '5':
                signal.number5(self)
            elif letter == '6':
                signal.number6(self)
            elif letter == '7':
                signal.number7(self)
            elif letter == '8':
                signal.number8(self)
            elif letter == '9':
                signal.number9(self)
            elif letter == '0':
                signal.number0(self)
            else:
                print("User entered an invalid character for morse code")
        #nextword()
        
    def close_application(self):
        GPIO.output(8,GPIO.LOW)
        GPIO.cleanup()
        self.close()        


app = QApplication(sys.argv) # The QApplication class manages the GUI application’s control flow and main settings.
screen = Window() # make screen grab class window
screen.show() # show window
sys.exit(app.exec_()) # allows system to exit app# this is needed otherwise you'll see something ugly
