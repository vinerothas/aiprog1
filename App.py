import functools
from BoardTriangle import BoardTriangle

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5 import QtCore


class App(object):

    def __init__(self, board):
        self.app = QApplication([])
        self.window = QWidget()
        self.board = board
        self.selected = None
        if type(board) is BoardTriangle:
            self.showTriangle()
        else:
            raise Exception('sum ting wong with board type, type is {}'.format(type(board)))
        self.window.show()
        self.app.exec_()

    def showTriangle(self):
        depth = self.board.depth
        layoutV = QVBoxLayout()
        for i in range(1, depth + 1):
            layoutH = QHBoxLayout()
            layoutV.addLayout(layoutH)
            layoutH.addStretch()
            for j in range(1, i + 1):
                button = QPushButton()
                peg = self.board.board[i - 1][j - 1]
                peg.button = button
                if peg.hasPeg:
                    button.setIcon(QIcon(QPixmap('peg.png')))
                else:
                    button.setIcon(QIcon(QPixmap('empty.png')))
                button.setIconSize(QSize(50, 50))
                button.clicked.connect(functools.partial(self.pegClick, peg))
                layoutH.addWidget(button)
            layoutH.addStretch()
        self.window.setLayout(layoutV)

    def pegClick(self, peg):
        print(peg.i, peg.j)
        if self.selected is not None:
            clearedPeg = self.getClearedPeg(peg)
            if clearedPeg is not None:
                peg.hasPeg = True
                peg.button.setIcon(QIcon(QPixmap('peg.png')))

                self.selected.hasPeg = False
                self.selected.button.setIcon(QIcon(QPixmap('empty.png')))
                self.selected = None

                clearedPeg.hasPeg = False
                clearedPeg.button.setIcon(QIcon(QPixmap('empty.png')))
            else:
                self.selected.button.setIcon(QIcon(QPixmap('peg.png')))
                self.selected = None
        else:
            if peg.hasPeg:
                peg.button.setIcon(QIcon(QPixmap('selected.png')))
                self.selected = peg
            else:
                self.selected.button.setIcon(QIcon(QPixmap('peg.png')))
                self.selected = None

    # returns None if invalid move
    def getClearedPeg(self, peg):
        if peg.hasPeg:
            return None
        i = self.selected.i
        j = self.selected.j
        i2 = peg.i
        j2 = peg.j
        if i2 == i + 2 and j2 == j + 2:
            cleared = self.board.board[i + 1][j + 1]
            if cleared.hasPeg:
                return cleared
            return None
        if i2 == i + 2 and j2 == j:
            cleared = self.board.board[i + 1][j]
            if cleared.hasPeg:
                return cleared
            return None
        if i2 == i and j2 == j + 2:
            cleared = self.board.board[i][j + 1]
            if cleared.hasPeg:
                return cleared
            return None
        if i2 == i and j2 == j - 2:
            cleared = self.board.board[i][j - 1]
            if cleared.hasPeg:
                return cleared
            return None
        if i2 == i - 2 and j2 == j:
            cleared = self.board.board[i - 1][j]
            if cleared.hasPeg:
                return cleared
            return None
        if i2 == i - 2 and j2 == j - 2:
            cleared = self.board.board[i - 1][j - 1]
            if cleared.hasPeg:
                return cleared
            return None
