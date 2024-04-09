import typing
import os
import json

from qtpy import QtGui, QtCore, QtWidgets

from Custom_Widgets.components.python.ui_emojiPicker import Ui_Form
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay


class QCustomEmojiPicker(QCustomTipOverlay):
    """A simple emoji picker"""

    def __init__(self, parent=None, target=None, tailPosition="top-center", itemsPerRow=8, performanceSearch=True, howForm=None):
        super().__init__(parent=parent, target=target, title='QCustom Emoji Picker', description='', isClosable=True, tailPosition=tailPosition, showForm=Ui_Form(), duration=-1)

        self.items_per_row = itemsPerRow
        self.performance_search = performanceSearch

        self.selected_emoji = None

        # connects `self.on_input(...)` whenever the search input text is changed
        self.form.form.search_line_edit.textChanged.connect(self.on_input)

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
            self.form.form.emoji_scroll_area_vlayout.addWidget(box)    

    def select(self) -> typing.Union[str, None]:
        """Shows this window and returns the selected emoji if a button was pressed or none, if the window was closed without choosing an emoji"""
        # should hide?
        return self.selected_emoji

    def on_input(self, text: str):
        """This method gets called if the text in the search input changes and selects all emojis which correspond with the search input text"""
        for i in range(self.form.form.emoji_scroll_area_vlayout.count()):
            group = self.form.form.emoji_scroll_area_vlayout.itemAt(i).widget()
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
            self.form.form.emoji_scroll_area_vlayout.insertWidget(0, search_results)

    class __QHoverPushButton(QtWidgets.QPushButton):
        """A custom QPushButton which detects when a mouse hovers it"""

        def __init__(self, text: str, parent_emoji_picker):
            """
            Args:
                text: The button text
                parent_emoji_picker (QCustomEmojiPicker): The parent emoji picker
            """
            super().__init__(text)
            self.clicked.connect(self.on_click)

            self.parent_emoji_picker = parent_emoji_picker

        def enterEvent(self, a0: QtCore.QEvent) -> None:
            """On mouse hover / when the mouse is over the button"""
            self.parent_emoji_picker.form.form.emoji_image_label.setText(self.text())
            group_title = self.parentWidget().title()
            # when the group title is 'Search results' the user has used the search input
            if group_title == 'Search results':
                self.parent_emoji_picker.form.form.emoji_name_label.setText(self.parent_emoji_picker.total_emojis[self.text()])
            else:
                self.parent_emoji_picker.form.form.emoji_name_label.setText(self.parent_emoji_picker.emojis[group_title][self.text()])

        def leaveEvent(self, a0: QtCore.QEvent) -> None:
            """When the mouse leaves the button"""
            self.parent_emoji_picker.form.form.emoji_image_label.setText('')
            self.parent_emoji_picker.form.form.emoji_name_label.setText('')

        def on_click(self):
            """Gets called if the button is pressed. Closes the emoji picker and if it was called via `QCustomEmojiPicker.select()` the current button emoji will be returned"""
            self.parent_emoji_picker.selected_emoji = self.text()
            # self.parent_emoji_picker.close()

            self.updateTargetText()

        def updateTargetText(self):
            target_widget = self.parent_emoji_picker.target
            emoji = self.parent_emoji_picker.selected_emoji
            
            # Check if the target widget is a QLineEdit
            if isinstance(target_widget, QtWidgets.QLineEdit):
                current_text = target_widget.text()
                new_text = current_text + emoji
                target_widget.setText(new_text)
                
            # Check if the target widget is a QTextEdit or QPlainTextEdit
            elif isinstance(target_widget, (QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
                cursor = target_widget.textCursor()
                cursor.insertText(emoji)
                
            # Add more conditions for other editable widgets if needed
            
            else:
                print("Target widget type not supported for text editing.")

