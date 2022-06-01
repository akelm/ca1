import os.path
from dataclasses import asdict
from pprint import pprint, pformat
from time import sleep

from PyQt5 import QtWidgets

import sys

from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.uic import loadUi

from add_log_level import addLoggingLevel
from calculate import calc
from parameters import Parameters
from params_mapping import getters

import logging
addLoggingLevel("custom", 51, methodName="custom")


# logging.basicConfig(filename='debug.txt', level="custom", format="%(message)s", filemode='w')
logging.basicConfig(filename='debug_tmp.txt', level=logging.DEBUG ,filemode='w')


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, params):
        super().__init__()
        self.params = params

    def run(self):
        """Long-running task."""
        calc(self.params)
        logging.debug("calc finished")
        self.finished.emit()


class UserInterface(QtWidgets.QMainWindow):




    def __init__(self):
        super(UserInterface, self).__init__()
        loadUi('untitled.ui', self)
        self.start_pushButton.clicked.connect(self.start)
        self.readca_btn.clicked.connect(self.getfile)
        self.readstr_btn.clicked.connect(self.getfile)
        self.debug_checkBox.stateChanged.connect(self.set_debug_btn)
        self.seedCheckBox.stateChanged.connect(lambda : self.seedLineEdit.setEnabled(self.seedCheckBox.isChecked()))
        self.show()

    def set_debug_btn(self):
        self.readca_btn.setEnabled(self.debug_checkBox.isChecked())
        self.readstr_btn.setEnabled(self.debug_checkBox.isChecked())

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Load array',
                                            '.')
        rel_file = os.path.relpath(fname[0])
        sender: QPushButton = self.sender()
        sender.setText(rel_file)




    def start(self):


        params_records = (
            (self.m2RowsLineEdit, "mrows"),
            (self.n2ColsLineEdit, "ncols"),
            (self.p_init_CLineEdit, "p_init_c"),
            (self.sharingCheckBox, "sharing"),
            (self.computationTypeComboBox, "competition_type"),
            (self.p_state_mutLineEdit, "p_state_mut"),
            (self.p_strat_mutLineEdit, "p_strat_mut"),
            (self.p_0_neighLineEdit, "p_0_neigh"),
            (self.num_of_iterLineEdit, "num_of_iter"),
            (self.num_of_experLineEdit, "num_of_exper"),
            (self.seedCheckBox, "if_seed"),
            (self.seedLineEdit, "seed"),

            (self.dd_penalty_lineEdit, "dd_penalty"),
            (self.dc_penalty_lineEdit, "dc_penalty"),
            (self.dd_reward_lineEdit, "dd_reward"),
            (self.dc_reward_lineEdit, "dc_reward"),
            (self.cd_reward_lineEdit, "cd_reward"),
            (self.cc_penalty_lineEdit, "cc_penalty"),
            (self.special_penalty_checkbox, "if_special_penalty"),
            (self.special_penalty_LineEdit, "special_penalty"),


            (self.allCLineEdit, "cc_penalty"),
            (self.allDLineEdit, "cc_penalty"),
            (self.kDLineEdit, "cc_penalty"),
            (self.kCLineEdit, "cc_penalty"),
            (self.kDCLineEdit, "cc_penalty"),
            (self.kconst_LineEdit, "k_const"),
            (self.kvar1_LineEdit, "k_var_0"),
            (self.kvar2_LineEdit, "k_var_1"),
            (self.k_buttonGroup, "k_change"),

            (self.species_comboBox, "species"),
            (self.level_LineEdit, "synchronization"),
            (self.debug_checkBox, "debug"),
            (self.readca_btn, "state_filename"),
            (self.readstr_btn, "strat_filename")

        )

        param_dict = {}

        for ui_object, param_object in params_records:
            ui_getter = getters[type(ui_object)]
            param_dict[param_object] = ui_getter(ui_object)

        params = Parameters(**param_dict).freeze()



        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(params)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        self.start_pushButton.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.start_pushButton.setEnabled(True)
        )








app = QtWidgets.QApplication(sys.argv)
window = UserInterface()
app.exec_()

