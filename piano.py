from PyQt5 import QtCore, QtMultimedia
import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog



class Example(QMainWindow, QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)


        # 1 октава, белые клавиши
        self.do('noty-do.mp3')
        self.pushButton_5.clicked.connect(self.player_do.play)

        self.re('re.mp3')
        self.pushButton_8.clicked.connect(self.player_re.play)

        self.mi('mi.mp3')
        self.pushButton_9.clicked.connect(self.player_mi.play)

        self.fa('fa.mp3')
        self.pushButton_10.clicked.connect(self.player_fa.play)

        self.sol('sol.mp3')
        self.pushButton_11.clicked.connect(self.player_sol.play)

        self.la('lja.mp3')
        self.pushButton_12.clicked.connect(self.player_la.play)

        self.si('si.mp3')
        self.pushButton_13.clicked.connect(self.player_si.play)


        # 1 октава, черные клавиши
        self.do_d('do_d.mp3')
        self.pushButton.clicked.connect(self.player_do_d.play)

        self.re_d('re_d.mp3')
        self.pushButton_2.clicked.connect(self.player_re_d.play)

        self.fa_d('fa_d.mp3')
        self.pushButton_3.clicked.connect(self.player_fa_d.play)

        self.sol_d('sol_d.mp3')
        self.pushButton_4.clicked.connect(self.player_sol_d.play)

        self.la_d('la_d.mp3')
        self.pushButton_6.clicked.connect(self.player_la_d.play)

        # Проверка нажатия на кнопку
        if e.key() == QtCore.Qt.Key_F:
            self.do('noty-do.mp3')

    def do(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_do = QtMultimedia.QMediaPlayer()
        self.player_do.setMedia(content)

    def re(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_re = QtMultimedia.QMediaPlayer()
        self.player_re.setMedia(content)

    def mi(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_mi = QtMultimedia.QMediaPlayer()
        self.player_mi.setMedia(content)

    def fa(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_fa = QtMultimedia.QMediaPlayer()
        self.player_fa.setMedia(content)

    def sol(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_sol = QtMultimedia.QMediaPlayer()
        self.player_sol.setMedia(content)

    def la(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_la = QtMultimedia.QMediaPlayer()
        self.player_la.setMedia(content)

    def si(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_si = QtMultimedia.QMediaPlayer()
        self.player_si.setMedia(content)


    def do_d(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_do_d = QtMultimedia.QMediaPlayer()
        self.player_do_d.setMedia(content)

    def re_d(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_re_d = QtMultimedia.QMediaPlayer()
        self.player_re_d.setMedia(content)

    def fa_d(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_fa_d = QtMultimedia.QMediaPlayer()
        self.player_fa_d.setMedia(content)

    def sol_d(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_sol_d = QtMultimedia.QMediaPlayer()
        self.player_sol_d.setMedia(content)

    def la_d(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player_la_d = QtMultimedia.QMediaPlayer()
        self.player_la_d.setMedia(content)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
