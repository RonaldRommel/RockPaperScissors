import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QImage, QBrush, QPalette, QPixmap, QIcon
from PyQt5.QtCore import QTimer

font = QFont("Times", 12)
btnstyle ='''QPushButton{
 padding: 1em 1.8em;
 outline: none;
 border: 1px solid #303030;
 background: #212121;
 color: #ae00ff;
 text-transform: uppercase;
 letter-spacing: 2px;
 font-size: 15px;
 overflow: hidden;
 transition: 0.2s;
 border-radius: 20px;
 cursor: pointer;
 font-weight: bold;
}
QPushButton:hover{
color:red;
background: rgba(33, 33, 33,0.9);
 transition-delay: 0.6s;
}
'''
font = QFont("Times", 14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.setWindowTitle("Rock Paper Scissors!!!")
        self.setGeometry(500, 200, 861, 661)
        self.UI()
        self.show()
        self.setWindowIcon(QIcon('images/game.ico'))
        oImage = QImage("images/game.jpg")
        self.setFixedSize(861,661)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)

    def UI(self):
        #################### BUTTONS #####################
        self.start = QPushButton("Start", self)
        self.stop = QPushButton("Stop", self)

        self.start.move(280,500)
        self.stop.move(480,500)

        self.start.setStyleSheet(btnstyle)
        self.stop.setStyleSheet(btnstyle)
        self.stop.setDisabled(True)

        self.start.clicked.connect(self.Start)
        self.stop.clicked.connect(self.Stop)

        ################# Label ########################
        self.image1 = QLabel(self)
        im1 = QPixmap("images/rock.png")
        self.image1.setPixmap(im1)
        self.image1.move(100, 150)
        self.image2 = QLabel(self)
        im2 = QPixmap("images/paper.png")
        self.image2.move(500, 150)
        self.image2.setPixmap(im2)

        ################# Text #####################
        self.cscore=0
        self.uscore=0
        self.comp = QLabel(self)
        self.comp.setText("Computer Score : {}".format(self.cscore))
        self.comp.move(170, 50)
        self.comp.setFont(font)
        self.comp.setStyleSheet("background-color: red;color:white;padding:5px;")

        self.user = QLabel(self)
        self.user.move(570, 50)
        self.user.setText("User Score : {}".format(self.uscore))
        self.user.setFont(font)
        self.user.setStyleSheet("background-color: blue;color:white;padding:5px")

        ############################# Timer #########################
        self.timer = QTimer(self)
        self.timer.setInterval(40)
        self.timer.timeout.connect(self.Timer)

    def Timer(self):
        gamedict={1: "images/rock.png", 2: "images/paper.png", 3: "images/scissors.png"}
        self.c = random.randint(1, 3)
        self.u = random.randint(1, 3)
        self.image1.setPixmap(QPixmap(gamedict[self.c]))
        self.image2.setPixmap(QPixmap(gamedict[self.u]))

    def Start(self):
        self.timer.start()
        self.stop.setEnabled(True)
        self.start.setDisabled(True)


    def Stop(self):
        self.timer.stop()
        self.CheckWinner()
        self.stop.setDisabled(True)
        self.start.setEnabled(True)



    def CheckWinner(self):
        if self.c == self.u:
            mbox = QMessageBox.question(self, "game", "Its a draw!!!", QMessageBox.Ok)
        elif (self.c == 1 and self.u == 2) or (self.c == 2 and self.u == 3) or (self.c == 3 and self.u == 1):
            mbox = QMessageBox.question(self, "game", "User Wins", QMessageBox.Ok)
            self.uscore +=1
            self.user.setText("User Score : {}".format(self.uscore))
        else:
            mbox = QMessageBox.question(self, "game", "Computer Wins", QMessageBox.Ok)
            self.cscore += 1
            self.comp.setText("Computer Score : {}".format(self.cscore))

        if self.cscore == 3 or self.uscore == 3:
            mbox = QMessageBox.question(self, "game", "Game Over!!! Start Another??", QMessageBox.Yes | QMessageBox.No)
            if mbox == QMessageBox.Yes:
                self.cscore = 0
                self.uscore = 0
                self.user.setText("User Score : {}".format(self.uscore))
                self.comp.setText("Computer Score : {}".format(self.cscore))
            else:
                self.close()
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()

