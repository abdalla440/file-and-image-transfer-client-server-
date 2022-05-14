import socket
import sys
import threading
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

# constants
# message type
TRANSFER = 20
#  header at the start of the message coming from the user tell the size of message
HEADER = 64
# set the port to the server
FORMAT = "utf-8"


class Client(QWidget):
    def __init__(self):
        super(Client, self).__init__()

        self.self_grid = QGridLayout(self)
        self.holder_frame = QFrame(self)
        self.holder_frame_grid = QGridLayout(self.holder_frame)
        self.message_viewer = QTextBrowser(self.holder_frame)
        self.header_label = QLabel(self.holder_frame)
        self.server_connection_frame = QFrame(self.holder_frame)
        self.server_connection_frame_holder = QGridLayout(self.server_connection_frame)
        self.connect_button = QPushButton(self.server_connection_frame)
        self.ip_input = QLineEdit(self.server_connection_frame)
        self.disconnect_button = QPushButton(self.server_connection_frame)
        self.port_input = QLineEdit(self.server_connection_frame)
        self.connect_label = QLabel(self.server_connection_frame)
        self.tabWidget = QTabWidget(self.holder_frame)
        self.file_tab = QWidget()
        self.file_tab_grid = QGridLayout(self.file_tab)
        self.select_file_button = QPushButton(self.file_tab)
        self.or_label = QLabel(self.file_tab)
        self.file_path_input = QLineEdit(self.file_tab)
        self.file_browser = QTextBrowser(self.file_tab)
        self.file_send_button = QPushButton(self.file_tab)
        self.image_tab = QWidget()
        self.image_tab_grid = QGridLayout(self.image_tab)
        self.select_image_button = QPushButton(self.image_tab)
        self.image_or_label = QLabel(self.image_tab)
        self.image_path_input = QLineEdit(self.image_tab)
        self.image_browser = QLabel(self.image_tab)
        self.image_send_button = QPushButton(self.image_tab)
        self.message_tab = QWidget()
        self.message_tab_grid = QGridLayout(self.message_tab)
        self.message_input = QTextEdit(self.message_tab)
        self.send_message_button = QPushButton(self.message_tab)

        self.set_features()
        self.retranslateUi()
        self.set_actions()

    def set_features(self):
        self.resize(908, 778)
        self.setStyleSheet(u"")
        self.self_grid.setObjectName(u"self_grid")
        self.self_grid.setContentsMargins(2, 2, 2, 2)
        self.holder_frame.setObjectName(u"holder_frame")
        self.holder_frame.setStyleSheet(u"QLabel{\n"
                                        "font:  \"Roboto\";\n"
                                        "color: rgb(52, 52, 52);\n"
                                        "font-size:14px;\n"
                                        "background-color: none;\n"
                                        "\n"
                                        "}\n"
                                        "QPushButton{\n"
                                        "border:1px solid  rgb(171, 173, 179);\n"
                                        "border-radius:6px;\n"
                                        "background-color:rgba(171, 173, 179, 0.4);\n"
                                        "width:80px;\n"
                                        "height:23px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "border:1px solid  rgb(0, 85, 0);\n"
                                        "background-color:rgba(171, 173, 179, 0.2);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "border:1px solid  rgb(0, 85, 0);\n"
                                        "background-color:rgba(171, 173, 179, 0.4);\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit{\n"
                                        "border:1px solid  rgb(171, 173, 179);\n"
                                        "font-family: Segoe ui;\n"
                                        "font-size: 15px;\n"
                                        "border-radius:6px;\n"
                                        "width:80px;\n"
                                        "height:23px;\n"
                                        "} \n"
                                        "\n"
                                        "QLineEdit:hover{\n"
                                        "background-color:rgba(171, 173, 179, 0.5);\n"
                                        "}\n"
                                        "")
        self.holder_frame.setFrameShape(QFrame.StyledPanel)
        self.holder_frame.setFrameShadow(QFrame.Raised)
        self.holder_frame_grid.setObjectName(u"holder_frame_grid")
        self.server_connection_frame.setObjectName(u"server_connection_frame")
        self.server_connection_frame.setStyleSheet(u"")
        self.server_connection_frame.setFrameShape(QFrame.StyledPanel)
        self.server_connection_frame.setFrameShadow(QFrame.Raised)
        self.server_connection_frame_holder.setObjectName(u"server_connection_frame_holder")
        self.server_connection_frame_holder.setContentsMargins(1, 1, 1, 17)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setStyleSheet(u"QPushButton{\n"
                                          "background-color: rgba(0, 85, 0,0.2);\n"
                                          "border:1px solid  rgb(0, 85, 0);\n"
                                          "border-radius:6px;\n"
                                          "width:80px;\n"
                                          "height:23px;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "background-color: rgba(0, 85, 0,0.1);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "background-color: rgba(0, 85, 0,0.2);\n"
                                          "}")

        self.server_connection_frame_holder.addWidget(self.connect_button, 1, 3, 1, 1)

        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setMinimumSize(QSize(0, 0))
        self.ip_input.setAlignment(Qt.AlignCenter)

        self.server_connection_frame_holder.addWidget(self.ip_input, 1, 1, 1, 1)

        self.disconnect_button.setObjectName(u"disconnect_button")
        self.disconnect_button.setStyleSheet(u"QPushButton{\n"
                                             "border:1px solid #b01e0b;\n"
                                             "border-radius:6px;\n"
                                             "background-color: rgba(176, 30, 11, 0.2);\n"
                                             "width:80px;\n"
                                             "height:23px;\n"
                                             "}\n"
                                             "QPushButton:hover {\n"
                                             "background-color: rgba(176, 30, 11, 0.1);\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "background-color: rgba(176, 30, 11, 0.2);\n"
                                             "}\n"
                                             "")

        self.server_connection_frame_holder.addWidget(self.disconnect_button, 1, 4, 1, 1)

        self.port_input.setObjectName(u"port_input")
        self.port_input.setMinimumSize(QSize(0, 0))
        self.port_input.setAlignment(Qt.AlignCenter)

        self.server_connection_frame_holder.addWidget(self.port_input, 1, 2, 1, 1)

        self.connect_label.setObjectName(u"connect_label")

        self.server_connection_frame_holder.addWidget(self.connect_label, 0, 1, 1, 2)

        self.server_connection_frame_holder.setColumnStretch(1, 2)
        self.server_connection_frame_holder.setColumnStretch(2, 2)
        self.server_connection_frame_holder.setColumnStretch(3, 1)
        self.server_connection_frame_holder.setColumnStretch(4, 1)

        self.holder_frame_grid.addWidget(self.server_connection_frame, 1, 0, 1, 2)

        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.file_tab.setObjectName(u"file_tab")
        self.file_tab_grid.setObjectName(u"file_tab_grid")
        self.select_file_button.setObjectName(u"select_file_button")

        self.file_tab_grid.addWidget(self.select_file_button, 0, 0, 1, 1)

        self.or_label.setObjectName(u"or_label")
        self.or_label.setAlignment(Qt.AlignCenter)

        self.file_tab_grid.addWidget(self.or_label, 0, 1, 1, 1)

        self.file_path_input.setObjectName(u"file_path_input")
        self.file_path_input.setAlignment(Qt.AlignCenter)

        self.file_tab_grid.addWidget(self.file_path_input, 0, 2, 1, 1)

        self.file_browser.setObjectName(u"file_browser")

        self.file_tab_grid.addWidget(self.file_browser, 1, 0, 1, 3)

        self.file_send_button.setObjectName(u"file_send_button")

        self.file_tab_grid.addWidget(self.file_send_button, 2, 0, 1, 3)

        self.tabWidget.addTab(self.file_tab, "")
        self.image_tab.setObjectName(u"image_tab")
        self.image_tab_grid.setObjectName(u"image_tab_grid")
        self.image_send_button.setObjectName(u"image_send_button")
        self.image_send_button.setStyleSheet(u"")

        self.image_tab_grid.addWidget(self.image_send_button, 2, 0, 1, 3)

        self.select_image_button.setObjectName(u"select_image_button")

        self.image_tab_grid.addWidget(self.select_image_button, 0, 0, 1, 1)

        self.image_path_input.setObjectName(u"image_path_input")
        self.image_path_input.setAlignment(Qt.AlignCenter)

        self.image_tab_grid.addWidget(self.image_path_input, 0, 2, 1, 1)

        self.image_or_label.setObjectName(u"image_or_label")
        self.image_or_label.setAlignment(Qt.AlignCenter)

        self.image_tab_grid.addWidget(self.image_or_label, 0, 1, 1, 1)

        self.image_browser.setObjectName(u"label")
        self.image_browser.setMaximumSize(QSize(416, 614))

        self.image_tab_grid.addWidget(self.image_browser, 1, 0, 1, 3)

        self.tabWidget.addTab(self.image_tab, "")
        self.message_tab.setObjectName(u"message_tab")
        self.message_tab_grid.setObjectName(u"message_tab_grid")
        self.message_input.setObjectName(u"message_input")

        self.message_tab_grid.addWidget(self.message_input, 0, 0, 1, 1)

        self.send_message_button.setObjectName(u"send_message_button")
        self.send_message_button.setStyleSheet(u"")

        self.message_tab_grid.addWidget(self.send_message_button, 1, 0, 1, 1)

        self.tabWidget.addTab(self.message_tab, "")

        self.holder_frame_grid.addWidget(self.tabWidget, 2, 0, 1, 1)

        self.message_viewer.setObjectName(u"message_browser")
        self.message_viewer.setStyleSheet("""
            font-size:15px;
            color: rgb(0, 85, 0);

        """)
        self.holder_frame_grid.addWidget(self.message_viewer, 2, 1, 1, 1)

        self.header_label.setObjectName(u"header_label")
        self.header_label.setMinimumSize(QSize(0, 50))
        self.header_label.setStyleSheet(u"font-size:25px;")
        self.header_label.setAlignment(Qt.AlignCenter)

        self.holder_frame_grid.addWidget(self.header_label, 0, 0, 1, 2)

        self.self_grid.addWidget(self.holder_frame, 0, 0, 1, 1)

        self.tabWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"Form", None))
        self.header_label.setText(QCoreApplication.translate("self", u" ----- Cilent Side -----", None))
        self.connect_button.setText(QCoreApplication.translate("self", u"Connect", None))
        self.ip_input.setPlaceholderText(QCoreApplication.translate("self", u"Enter server IP", None))
        self.disconnect_button.setText(QCoreApplication.translate("self", u"Disconnect", None))
        self.port_input.setText("")
        self.port_input.setPlaceholderText(QCoreApplication.translate("self", u"Enter server Port", None))
        self.connect_label.setText(QCoreApplication.translate("self", u"connect to the server", None))
        self.select_file_button.setText(QCoreApplication.translate("self", u"Select file", None))
        self.or_label.setText(QCoreApplication.translate("self", u"or  ", None))
        self.file_path_input.setPlaceholderText(QCoreApplication.translate("self", u"Enter File Path", None))
        self.file_send_button.setText(QCoreApplication.translate("self", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.file_tab),
                                  QCoreApplication.translate("self", u"file transfer", None))
        self.select_image_button.setText(QCoreApplication.translate("self", u"Select image", None))
        self.image_or_label.setText(QCoreApplication.translate("self", u"or  ", None))
        self.image_path_input.setPlaceholderText(QCoreApplication.translate("self", u"Enter Image Path", None))
        self.image_send_button.setText(QCoreApplication.translate("self", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.image_tab),
                                  QCoreApplication.translate("self", u"image transfer", None))
        self.send_message_button.setText(QCoreApplication.translate("self", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.message_tab),
                                  QCoreApplication.translate("self", u"message transfer", None))

    def set_actions(self):
        self.select_file_button.clicked.connect(lambda: self.browse("file"))
        self.select_image_button.clicked.connect(lambda: self.browse("image"))
        self.connect_button.clicked.connect(lambda: self.connect_server())
        self.disconnect_button.clicked.connect(lambda: self.send_msg(msg="!DISCONNECT"))
        self.send_message_button.clicked.connect(lambda: self.send_msg(msg=self.message_input.toPlainText()))
        self.image_send_button.clicked.connect(lambda: self.send_img())
        self.file_send_button.clicked.connect(lambda: self.send_file())

    def connect_server(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # ADDR (SERVER IP, SERVER PORT)
            self.message_viewer.append(f"[CONNECTING] connecting the server...")
            ADDR = (self.ip_input.text(), int(self.port_input.text()))
            self.client_socket.connect(ADDR)
            self.message_viewer.append(f"[CONNECTING] connected successfully\n")
        except:
            self.message_viewer.append(f"[Warning] can't connect the server!!!!!\n")

    def browse(self, flag):
        # get opened file path
        file_path = QFileDialog.getOpenFileName(self, "open file")[0]
        if file_path:
            if flag == "file":
                self.file_path_input.setText(file_path)
                with open(file_path, "r") as file:
                    file_content = file.read()
                self.file_browser.setText(file_content)
                self.message_viewer.append("[OPEN FILE] file opened successfully\n")

            if flag == "image":
                self.image_path_input.setText(file_path)
                pixmap = QPixmap(file_path)
                self.image_browser.setPixmap(pixmap)
                self.message_viewer.append("[OPEN IMAGE] image opened successfully\n")

    def send_msg(self, msg):
        try:
            # encode the message into byte-like format
            message = msg.encode(FORMAT)
            # get the length of the message
            msg_length = len(message)
            # encode message length into string "utf-8"
            send_length = str(msg_length).encode(FORMAT)
            # pad the length to 64 bytes long
            # here you get the difference between Header size and your send_length then add the rest of it as spaces
            send_length += b' ' * (HEADER - len(send_length))  # b' ' byte representation of the string (space)
            # send ack that you will send a message
            self.client_socket.send("message".encode(FORMAT) + b' ' * (TRANSFER - len("message")))
            self.message_viewer.append("[SENDING] MESSAGE")

            # send the header to the server
            self.client_socket.send(send_length)
            self.message_viewer.append(f"[SENDING MESSAGE HEADER] {send_length}")

            # send actual message to the server
            self.client_socket.send(message)
            self.message_viewer.append(f"[SENDING MESSAGE] {message}")

            # ack that server's message is here
            self.message_viewer.append(self.client_socket.recv(2048).decode(FORMAT)+"\n")
        except:
            self.message_viewer.append(f"[Warning] can't send the message!!!!!\n")

    def send_file(self):
        try:
            # send ack that you will send a file
            self.client_socket.send("file".encode(FORMAT) + b' ' * (TRANSFER - len("file")))
            self.message_viewer.append("[SENDING] FILE")

            file_path = self.file_path_input.text()

            # get file content
            with open(file_path, "r") as opened_file:
                #
                file_data = opened_file.read()
                # create file name
                file_name = opened_file.name.split("/")[-1]

            # send filename to the server
            self.client_socket.send(file_name.encode(FORMAT))
            self.message_viewer.append(f"[SENDING FILE NAME] {file_name}")

            # get the length of the file
            file_length = len(file_data)

            # encode file length into string "utf-8"
            send_length = str(file_length).encode(FORMAT)

            # pad the length to 64 bytes long
            # here you get the difference between Header size and your send_length then add the rest of it as spaces
            send_length += b' ' * (HEADER - len(send_length))  # b' ' byte representation of the string (space)

            # send the header to the server
            self.client_socket.send(send_length)
            self.message_viewer.append(f"[SENDING FILE HEADER] {send_length}")

            # send file content to the server
            self.client_socket.send(file_data.encode(FORMAT))
            self.message_viewer.append(f"[SENDING FILE DATA] file data sent successfully")

            # ack that server's message is here
            self.message_viewer.append(self.client_socket.recv(2048).decode(FORMAT)+"\n")
        except:
            self.message_viewer.append(f"[Warning] can't send the file!!!!!\n")
    def send_img(self):
        try:
            # send ack that you will send a image
            self.client_socket.send("image".encode(FORMAT) + b' ' * (TRANSFER - len("image")))
            self.message_viewer.append("[SENDING] IMAGE")

            img_path = self.image_path_input.text()
            # get file content
            file = open(img_path, "rb")
            # get image data (pixels)
            img_data = file.read(40411)

            # create image name
            img_name = file.name.split("/")[-1]

            # send filename to the server
            self.client_socket.send(img_name.encode(FORMAT))
            self.message_viewer.append(f"[SENDING IMAGE NAME] {img_name}")

            # get the length of the image
            img_length = len(img_data)

            # encode image length into string "utf-8"
            send_length = str(img_length).encode(FORMAT)

            # pad the length to 64 bytes long
            # here you get the difference between Header size and your send_length then add the rest of it as spaces
            send_length += b' ' * (HEADER - len(send_length))  # b' ' byte representation of the string (space)

            # send the header to the server
            self.client_socket.send(send_length)
            self.message_viewer.append(f"[SENDING IMAGE HEADER] {send_length}")

            # send image content to the server
            self.client_socket.send(img_data)
            self.message_viewer.append(f"[SENDING IMAGE DATA] image data sent successfully")

            file.close()

            # ack that server's message is here
            self.message_viewer.append(self.client_socket.recv(2048).decode(FORMAT)+"\n")
        except:
            self.message_viewer.append(f"[Warning] can't send the image!!!!!\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    client = Client()
    client.show()

    sys.exit(app.exec_())
