#                 qtpy Custom Widgets                #
#                GPL 3.0 - Kadir Aksoy                #
#   https://github.com/kadir014/pyqt5-custom-widgets  #
#  DISCLAIMER: This class uses the JSON files in the  #
#              syntax and themes folders which has    #
#              pre-defined syntax rules and themes.   #
#              Don't forget to include them in your   #
#              package's folder if you're installing  #
#              this project manually.  

import json
import pathlib

from qtpy.QtCore import QRegularExpression, Qt
from qtpy.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPlainTextEdit
from qtpy.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter, QPainter, QPen, QBrush 

class QCustomCodeEditor(QWidget):

    LANG_DISPLAY = {
            "plain"  : "Plain text",
            "python" : "Python",
            "py"     : "Python",
            "cpp"    : "C++",
            "c++"    : "C++"
        }

    def __init__(self):
        super().__init__()

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.layout.addSpacing(37)

        self.editorlyt = QVBoxLayout()
        self.editorlyt.setSpacing(0)
        self.editorlyt.setContentsMargins(0, 0, 0, 0)
        self.layout.addLayout(self.editorlyt)

        self.editor = QPlainTextEdit()
        self.editor.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.editorlyt.addWidget(self.editor)

        self.setStyleSheet("QPlainTextEdit {font-family:Consolas; font-size:14px; color:#222222;}")

        self.highlighter = QCustomSyntaxHighlighter(self.editor.document())

        self.sliderVal = 0
        self.lastdigit = 2
        vs = self.editor.verticalScrollBar()

        @vs.rangeChanged.connect
        def slot(v):
            self.sliderVal = self.editor.verticalScrollBar().value()

            if len(str(vs.maximum()+15)) > self.lastdigit:
                self.lastdigit = len(str(vs.maximum()+15))
                self.layout.insertSpacing(0, 10)

            self.update()

        @vs.valueChanged.connect
        def slot(v):
            self.sliderVal = v

            self.update()

        self.statusbar = QWidget()
        self.statusbar.setFixedHeight(26)
        self.statusbarlyt = QHBoxLayout()
        self.statusbarlyt.setContentsMargins(10, 0, 30, 0)
        self.statusbar.setLayout(self.statusbarlyt)
        self.editorlyt.addWidget(self.statusbar)

        self.cursor_lbl = QLabel("0:0")
        self.cursor_lbl.setStyleSheet("font-size:16px;")
        self.statusbarlyt.addWidget(self.cursor_lbl, alignment=Qt.AlignLeft|Qt.AlignVCenter)

        self.lang_lbl = QLabel("Plain text")
        self.lang_lbl.setStyleSheet("font-size:16px;")
        self.statusbarlyt.addWidget(self.lang_lbl, alignment=Qt.AlignRight|Qt.AlignVCenter)

        @self.editor.cursorPositionChanged.connect
        def slot():
            self.cursor_lbl.setText(f"{self.editor.textCursor().blockNumber()}:{self.editor.textCursor().positionInBlock()}")

    def __repr__(self):
        return f"<Custom.CodeTextEdit({QCustomCodeEditor.LANG_DISPLAY(self.lang)})>"

    def setTheme(self, theme):
        self.highlighter.setTheme(theme)
        self.highlighter.setRules()

        c = self.highlighter.theme["background"]
        rgb = f"rgb({c.red()}, {c.green()}, {c.blue()})"

        cc = self.highlighter.theme["identifier"]
        crgb = f"rgb({cc.red()}, {cc.green()}, {cc.blue()})"

        self.editor.setStyleSheet(f"QPlainTextEdit {{background-color: {rgb}; color: {crgb};}}")

        self.cursor_lbl.setStyleSheet(f"color: {crgb}; font-size:16px;")
        self.lang_lbl.setStyleSheet(f"color: {crgb}; font-size:16px;")

        self.highlighter.rehighlight()
        self.update()

    def setLang(self, lang):
        self.lang_lbl.setText(QCustomCodeEditor.LANG_DISPLAY[lang])

        self.highlighter.setLang(lang)
        self.highlighter.setRules()
        self.highlighter.rehighlight()
        self.update()

    def loadFile(self, filepath, encoding="utf-8"):

        if filepath.endswith(".py"): lang = "python"
        elif filepath.endswith(".cpp"): lang = "cpp"
        else: lang = "plain"

        with open(filepath, "r", encoding=encoding) as f:
            self.editor.setPlainText(f.read())

        self.setLang(lang)

    def paintEvent(self, event):
        pt = QPainter()
        pt.begin(self)
        pt.setRenderHint(QPainter.Antialiasing)

        pt.setBrush(QBrush(self.highlighter.theme["lines-background"]))

        pt.drawRect(0, 0, self.width(), self.height())

        font = self.editor.font()
        pt.setFont(font)

        gap = font.pixelSize() + 3

        for i in range((self.height()//gap)):
            font = pt.font()
            pt.setFont(font)
            pt.setPen(QPen(self.highlighter.theme["lines"]))

            pt.drawText(13, i*gap, str(i+self.sliderVal))

        pt.setBrush(QBrush(self.highlighter.theme["background"]))
        pt.setPen(QPen(QColor(0, 0, 0, 0)))
        pt.drawRect(3, self.height()-self.statusbar.height(), 40, self.statusbar.height()-6)

        pt.end()

class QCustomSyntaxHighlighter(QSyntaxHighlighter):

    AVAILABLE_LANGS = {
            "plain"  : "plain",
            "py"     : "python",
            "python" : "python",
            "cpp"    : "cpp",
            "c++"    : "cpp"
        }

    def __init__(self, document, lang="python", theme="default"):
        super().__init__(document)

        self.setLang(lang)
        self.setTheme(theme)
        self.setRules()

    def formatThemeKey(self, color, style="", returnColor=False):
        _color = QColor()
        if type(color) is not str:
            _color.setRgb(color[0], color[1], color[2])

        elif color.startswith("#"):
            hexc = color.lstrip('#')
            hexc = tuple(int(hexc[i:i+2], 16) for i in (0, 2, 4))
            _color.setRgb(*hexc)

        else:
            _color.setNamedColor(color)

        if returnColor: return _color

        _format = QTextCharFormat()
        _format.setForeground(_color)
        if "bold"   in style: _format.setFontWeight(QFont.Bold)
        if "italic" in style: _format.setFontItalic(True)

        return _format

    def setTheme(self, theme):
        if isinstance(theme, dict):
            pass

        else:
            path = pathlib.Path(__file__).parents[0] / "CodeEditorThemes" / f"{theme}.json"
            with open(path, "r", encoding="utf-8") as f:
                s = json.loads(f.read())

                self.theme = dict()

                for k in s:
                    p = s[k].split("-")
                    if len(p) == 2: self.theme[k] = self.formatThemeKey(s[k], p[1])
                    else: self.theme[k] = self.formatThemeKey(s[k])

                self.theme["background"] = self.formatThemeKey(s["background"], returnColor=True)
                self.theme["lines-background"] = self.formatThemeKey(s["lines-background"], returnColor=True)
                self.theme["lines"] = self.formatThemeKey(s["lines"], returnColor=True)
                self.theme["identifier"] = self.formatThemeKey(s["identifier"], returnColor=True)

    def setLang(self, lang):
        lang = lang.lower()

        if lang in QCustomSyntaxHighlighter.AVAILABLE_LANGS:
            self.lang = QCustomSyntaxHighlighter.AVAILABLE_LANGS[lang]

            if self.lang == "plain": return

            path = pathlib.Path(__file__).parents[0] / "CodeEditorSyntax" / f"{self.lang}.json"
            with open(path, "r", encoding="utf-8") as f:
                rr = json.loads(f.read())

                self.keywords = rr["keywords"]
                self.this = rr["this"]
                self.comment = rr["comment"]

            self.operators = operators = (
                    "=",
                    "==", "!=", "<", "<=", ">", ">=",
                    "\+", "-", "\*", "/", "//", "\%", "\*\*",
                    "\+=", "-=", "\*=", "/=", "\%=",
                    "\^", "\|", "\&", "\~", ">>", "<<",
                    "\+\+", "--", "\&\&", "\|\|"
                )

            self.braces = (
                    "\{", "\}", "\(", "\)", "\[", "\]",
                )

        else:
            raise ValueError(f"Language '{lang}' is not supported.")

    def setRules(self):
        self.tri_single = (QRegularExpression("'''"), 1, self.theme["string"])
        self.tri_double = (QRegularExpression('"""'), 2, self.theme["string"])

        if self.lang == "plain":
            self.rules = list()
            return

        rules = list()

        rules += [(r'\b%s\b' % w, 0, self.theme["keyword"])  for w in self.keywords]

        rules += [(r'%s' % o,     0, self.theme["operator"]) for o in self.operators]

        rules += [(r'%s' % b,     0, self.theme["brace"])    for b in self.braces]

        if self.lang in ("cpp", "c"):
            rules.append( (r'\#[^\n]*', 0, self.theme["preprocessor"]) )

        rules += [
            (r"\b[A-Za-z0-9_]+(?=\()",  0, self.theme["function"]),

            (r'\b%s\b' % self.this,     0, self.theme["this"]),

            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, self.theme["string"]),

            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, self.theme["string"]),

            (r'%s[^\n]*' % self.comment, 0, self.theme["comment"]),

            (r'\b[+-]?[0-9]+[lL]?\b',                             0, self.theme["numeric"]),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b',                  0, self.theme["numeric"]),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, self.theme["numeric"])
        ]

        self.rules = [(QRegularExpression(pat), index, fmt) for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        for expression, nth, format in self.rules:
            match = expression.match(text)
            index = match.capturedStart(nth)

            while index >= 0:
                length = match.capturedLength(nth)
                self.setFormat(index, length, format)
                index = expression.match(text, index + length).capturedStart(nth)

        self.setCurrentBlockState(0)

        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)



    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0

        else:
            match = delimiter.match(text)
            start = match.capturedStart()
            add = match.capturedLength()

        while start >= 0:
            end = delimiter.indexIn(text, start + add)

            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)

            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add

            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)


        if self.currentBlockState() == in_state: return True
        else: return False
