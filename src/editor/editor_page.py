import typing
from PySide6 import QtCore, QtWidgets

from editor.ui_editor_page import Ui_EditorPage


class EditorPage(QtWidgets.QWidget):
    send_flow_to_editor = QtCore.Signal(object)
    send_flow_to_fuzzer = QtCore.Signal(object)

    def __init__(self, *args: typing.Any, **kwargs: typing.Any):
        super(EditorPage, self).__init__(*args, **kwargs)

        self.ui = Ui_EditorPage()
        self.ui.setupUi(self)

    def about_to_quit(self):
        pass
