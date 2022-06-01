# from ca_gui import UserInterface
# from parameters import Parameters
from PyQt5.QtWidgets import QLineEdit, QCheckBox, QComboBox, QButtonGroup, QPushButton

getters = dict((
              (QLineEdit, lambda x : float(QLineEdit.text(x)) if QLineEdit.text(x) else -1),
              (QCheckBox, QCheckBox.isChecked ),
              (QComboBox, QComboBox.currentIndex),
              (QButtonGroup, lambda x: -QButtonGroup.checkedId(x) -2),
              (QPushButton, QPushButton.text)
))





# int(QLineEdit.text())