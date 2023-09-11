from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFrame)
from pagina_principal import Ui_MainWindow




class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define a aparência da janela
        self.setStyleSheet("background-color: #202020; color: #fff; font-size: 16px;")
        self.setFixedSize(800, 500)
        self.setWindowTitle("Autenticação")

        # Define o frame que contém a imagem de fundo
        frame = QFrame(self)
        frame.setGeometry(0, 0, 800, 500)
        frame.setStyleSheet("background-image: url(background.jpg);")

        # Define os elementos da janela de login
        self.label_username = QLabel("Usuário:", self)
        self.label_username.move(320, 200)
        self.line_edit_username = QLineEdit(self)
        self.line_edit_username.move(400, 200)
        self.label_password = QLabel("Senha:", self)
        self.label_password.move(320, 250)
        self.line_edit_password = QLineEdit(self)
        self.line_edit_password.move(400, 250)
        self.line_edit_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Entrar", self)
        self.button_login.move(400, 310)
        self.button_login.clicked.connect(self.login)

    def login(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()
        if username == "admin" and password == "1234":
            self.new_window = MainWindow()
            self.new_window.show()
            self.close()

        else:
            print("Nome de usuário ou senha inválidos.")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



if __name__ == '__main__':

    app = QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec()