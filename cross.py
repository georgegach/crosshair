import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=2):
        QtWidgets.QWidget.__init__(self, parent)
        self.ws = windowSize
        self.resize(windowSize, windowSize)
        self.pen = QtGui.QPen(QtGui.QColor(100,255,100,150))                
        self.pen.setWidth(penWidth)                                            
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center())


    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        # painter.drawLine(x1,y1, x2,y2)
        painter.drawLine(self.ws/2, 0, self.ws/2, self.ws/2-self.ws/6)          # Top
        painter.drawLine(self.ws/2, self.ws/2+self.ws/6, self.ws/2, self.ws)    # Bottom
        painter.drawLine(0, self.ws/2, self.ws/2 - self.ws/6, self.ws/2)        # Left
        painter.drawLine(self.ws/2 + self.ws/6, self.ws/2, self.ws, self.ws/2)  # Right


app = QtWidgets.QApplication(sys.argv) 

widget = Crosshair(windowSize=24, penWidth=2)
widget.show()

sys.exit(app.exec_())
