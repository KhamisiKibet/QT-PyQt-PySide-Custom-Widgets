from qtpy import QtGui, QtCore, QtWidgets
import typing
import os
import json


class QEmojiPicker(QtWidgets.QDialog):
    """A simple emoji picker"""

    def __init__(self, parent: QtWidgets = None, flags: typing.Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType] = None, items_per_row=8, performance_search=True):
        """
        Args:
            parent: The parent window
            flags: Qt flags
            items_per_row: How many items per row should be displayed
            performance_search: If True, the search input will display the emojis faster. See `self.on_input(...)` for more details
        """
        if flags:
            super().__init__(parent, flags)
        else:
            super().__init__(parent)
        # initializes the ui
        self.setupUi(self)
        self.retranslateUi(self)

        self.items_per_row = items_per_row
        self.performance_search = performance_search

        self.selected_emoji = None

        # connects `self.on_input(...)` whenever the search input text is changed
        self.search_line_edit.textChanged.connect(self.on_input)

        # the emojis.
        current_script = os.path.dirname(os.path.realpath(__file__))
        jsonFile = os.path.abspath(os.path.join(str(current_script), 'components/json/emojis.json'))
        with open(jsonFile, encoding='utf-8') as jsonFile:
            self.emojis = json.load(jsonFile)

        self.total_emojis = {}

        for group, items in self.emojis.items():
            box = QtWidgets.QGroupBox(group)
            layout = QtWidgets.QGridLayout()
            for i, (emoji, name) in enumerate(items.items()):
                # uses a little modified push button which recognizes when the mouse is over the button
                button = self.__QHoverPushButton(text=emoji, parent_emoji_picker=self)

                button.setFlat(True)
                button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                button.setFixedSize(30, 30)
                # the button style
                button.setStyleSheet('QPushButton {'
                                     '  font-size: 20px;'
                                     '  border-radius: 50%%;'
                                     '}'
                                     'QPushButton:hover {'
                                     '  background-color: %s'
                                     '}' % button.palette().button().color().darker().name())
                layout.addWidget(button, int(i / self.items_per_row), i % self.items_per_row)

                # adds the current emoji with its name to a dict where are all emojis without groups are listed
                self.total_emojis[emoji] = name

                box.setLayout(layout)
            self.emoji_scroll_area_vlayout.addWidget(box)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_line_edit = QtWidgets.QLineEdit(Form)
        self.search_line_edit.setObjectName("search_line_edit")
        self.verticalLayout.addWidget(self.search_line_edit)
        self.emoji_scroll_area = QtWidgets.QScrollArea(Form)
        self.emoji_scroll_area.setWidgetResizable(True)
        self.emoji_scroll_area.setObjectName("emoji_scroll_area")
        self.emoji_scroll_area_widgets = QtWidgets.QWidget()
        self.emoji_scroll_area_widgets.setGeometry(QtCore.QRect(0, 0, 384, 198))
        self.emoji_scroll_area_widgets.setObjectName("emoji_scroll_area_widgets")
        self.emoji_scroll_area_vlayout = QtWidgets.QVBoxLayout(self.emoji_scroll_area_widgets)
        self.emoji_scroll_area_vlayout.setObjectName("emoji_scroll_area_vlayout")
        self.emoji_scroll_area.setWidget(self.emoji_scroll_area_widgets)
        self.verticalLayout.addWidget(self.emoji_scroll_area)
        self.emoji_information_hlayout = QtWidgets.QHBoxLayout()
        self.emoji_information_hlayout.setObjectName("emoji_information_hlayout")
        self.emoji_image_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emoji_image_label.sizePolicy().hasHeightForWidth())
        self.emoji_image_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.emoji_image_label.setFont(font)
        self.emoji_image_label.setText("")
        self.emoji_image_label.setObjectName("emoji_image_label")
        self.emoji_information_hlayout.addWidget(self.emoji_image_label)
        self.emoji_name_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emoji_name_label.sizePolicy().hasHeightForWidth())
        self.emoji_name_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.emoji_name_label.setFont(font)
        self.emoji_name_label.setText("")
        self.emoji_name_label.setObjectName("emoji_name_label")
        self.emoji_information_hlayout.addWidget(self.emoji_name_label)
        self.verticalLayout.addLayout(self.emoji_information_hlayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.search_line_edit.setPlaceholderText(_translate("Form", "Search..."))

    def select(self) -> typing.Union[str, None]:
        """Shows this window and returns the selected emoji if a button was pressed or none, if the window was closed without choosing an emoji"""
        self.exec()
        return self.selected_emoji

    def on_input(self, text: str):
        """This method gets called if the text in the search input changes and selects all emojis which correspond with the search input text"""
        for i in range(self.emoji_scroll_area_vlayout.count()):
            group = self.emoji_scroll_area_vlayout.itemAt(i).widget()
            # hides and deletes the previous 'Search results' group box
            if group.title() == 'Search results':
                group.hide()
                group.deleteLater()
            # if no text is given / the search input is empty, every group which is hidden will be shown
            elif not text and group.isHidden():
                group.show()
            # if a text is given / the search input has text, every group which is not hidden will be shown
            elif text and not group.isHidden():
                group.hide()

        if text:
            search_results = QtWidgets.QGroupBox('Search results')
            layout = QtWidgets.QGridLayout()

            items = -1

            def add_item():
                # `items` is readonly in inner functions, so it can't increased here and has to be increases in the two loop below

                # uses a little modified push button which recognizes when the mouse is over the button
                button = self.__QHoverPushButton(text=emoji, parent_emoji_picker=self)

                button.setFlat(True)
                button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                button.setFixedSize(30, 30)
                # the button style
                button.setStyleSheet('QPushButton {'
                                     '  font-size: 20px;'
                                     '  border-radius: 50%%;'
                                     '}'
                                     'QPushButton:hover {'
                                     '  background-color: %s'
                                     '}' % button.palette().button().color().darker().name())
                layout.addWidget(button, int(items / self.items_per_row), items % self.items_per_row)

            lower_text = text.lower()
            # if `self.performance_search` is True, only emoji names starting with the specified text are displayed
            if self.performance_search:
                for emoji, name in self.total_emojis.items():
                    if name.lower().startswith(lower_text):
                        items += 1
                        add_item()
            # but if `self.performance_search` is False, emoji texts which containing the specified text are displayed
            else:
                for emoji, name in self.total_emojis.items():
                    if lower_text in name.lower():
                        items += 1
                        add_item()

            # adds a spacer below the found emojis to "order" them properly
            layout.addItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding), int(items / self.items_per_row) + 1, 0, columnSpan=self.items_per_row)

            search_results.setLayout(layout)
            self.emoji_scroll_area_vlayout.insertWidget(0, search_results)

    class __QHoverPushButton(QtWidgets.QPushButton):
        """A custom QPushButton which detects when a mouse hovers it"""

        def __init__(self, text: str, parent_emoji_picker):
            """
            Args:
                text: The button text
                parent_emoji_picker (QEmojiPicker): The parent emoji picker
            """
            super().__init__(text)
            self.clicked.connect(self.on_click)

            self.parent_emoji_picker = parent_emoji_picker

        def enterEvent(self, a0: QtCore.QEvent) -> None:
            """On mouse hover / when the mouse is over the button"""
            self.parent_emoji_picker.emoji_image_label.setText(self.text())
            group_title = self.parentWidget().title()
            # when the group title is 'Search results' the user has used the search input
            if group_title == 'Search results':
                self.parent_emoji_picker.emoji_name_label.setText(self.parent_emoji_picker.total_emojis[self.text()])
            else:
                self.parent_emoji_picker.emoji_name_label.setText(self.parent_emoji_picker.emojis[group_title][self.text()])

        def leaveEvent(self, a0: QtCore.QEvent) -> None:
            """When the mouse leaves the button"""
            self.parent_emoji_picker.emoji_image_label.setText('')
            self.parent_emoji_picker.emoji_name_label.setText('')

        def on_click(self):
            """Gets called if the button is pressed. Closes the emoji picker and if it was called via `QEmojiPicker.select()` the current button emoji will be returned"""
            self.parent_emoji_picker.selected_emoji = self.text()
            self.parent_emoji_picker.close()
