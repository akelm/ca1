import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, \
    QHBoxLayout, QLabel, QFormLayout, QCheckBox, QButtonGroup, QRadioButton

import matplotlib

from mpl_canvas import MplCanvas

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

# Create a subclass of QMainWindow to setup the calculator's GUI
class PyCalcUi(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Domino Problem')
        # self.setFixedSize(235, 235)
        # Set the central widget and the general layout
        self.generalLayout = QHBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._create_parameters_layout()
        self._create_strategies_layout()
        self.create_canvas_layout()
        # self._createDisplay()
        # self._createButtons()

        self.states_list = []
        self.strategies_list = []


    def create_canvas_layout(self):
        v_layout = QVBoxLayout()
        self.generalLayout.addLayout(v_layout)

        h_layout = QHBoxLayout()
        self.canvas_button_group = QButtonGroup()
        states_but = QRadioButton("States")
        strategies_but = QRadioButton("Strategies")
        kd_str_but = QRadioButton("k-D strat.")
        kc_str_but = QRadioButton("k-C strat.")
        kdc_str_but = QRadioButton("k-DC strat.")
        for widget in states_but, strategies_but, kd_str_but, kc_str_but, kdc_str_but:
            h_layout.addWidget(widget)
            self.canvas_button_group.addButton(widget)

        v_layout.addLayout(h_layout)
        self.canvas = MplCanvas()
        v_layout.addWidget(self.canvas)

        grid = QGridLayout()
        v_layout.addLayout(grid)

        hl = QHBoxLayout()
        hl.addWidget(QLabel("iter step"))
        self.iter_step = QLineEdit()
        hl.addWidget(self.iter_step)
        grid.addLayout(hl, 0, 0)

        self.start_animation = QPushButton("Start animation")
        self.stop_animation = QPushButton("Stop animation")
        self.save_statistics = QPushButton("Save statistics")
        self.save_pictures = QPushButton("Save pictures")

        grid.addWidget(self.start_animation, 0, 1)
        grid.addWidget(self.stop_animation, 1, 1)
        grid.addWidget(self.save_statistics, 2,0)
        grid.addWidget(self.save_pictures, 2,1)

    def _create_strategies_layout(self):
        v_layout = QFormLayout()
        self.generalLayout.addLayout(v_layout)

        v_layout.addRow(QLabel("Strategies"))

        self.all_c = QLineEdit()
        v_layout.addRow(QLabel("all-C"), self.all_c)

        self.all_d = QLineEdit()
        v_layout.addRow(QLabel("all-D"), self.all_d)

        self.k_d = QLineEdit()
        v_layout.addRow(QLabel("k-D"), self.k_d)

        self.k_c = QLineEdit()
        v_layout.addRow(QLabel("k-C"), self.k_c)

        self.k_dc = QLineEdit()
        v_layout.addRow(QLabel("k-DC"), self.k_dc)

        btn_group = QButtonGroup()
        self.k_const = QRadioButton()
        self.k_const.setText("k_const")
        self.k_var = QRadioButton()
        self.k_var.setText("k_var")
        btn_group.addButton(self.k_const)
        btn_group.addButton(self.k_var)

        self.k_const_edit = QLineEdit()
        v_layout.addRow(self.k_const, self.k_const_edit)

        self.k_var_edit_1 = QLineEdit()
        self.k_var_edit_2 = QLineEdit()

        v_layout.addRow(self.k_var, self.k_var_edit_1)
        v_layout.addRow(QLabel(), self.k_var_edit_2)

        v_layout.addRow(QLabel("Species"))
        self.species_btn_group = QButtonGroup()
        b1 = QRadioButton("type 1")
        self.species_btn_group.addButton(b1)
        v_layout.addRow(b1, QLabel("▀"))
        b2 = QRadioButton("type 2")
        self.species_btn_group.addButton(b2)
        v_layout.addRow(b2, QLabel("▀▀"))
        b2 = QRadioButton("type 2")
        self.species_btn_group.addButton(b2)
        v_layout.addRow(b2, QLabel("▌"))

        self.debug_button = QCheckBox("Debug")
        v_layout.addRow(self.debug_button)
        self.debug_button_group = QButtonGroup()
        b_random = QRadioButton("random init")
        b_deter = QRadioButton("deterministic init")
        self.debug_button_group.addButton(b_random)
        self.debug_button_group.addButton(b_deter)
        v_layout.addRow(b_random)
        v_layout.addRow(b_deter)

        self.read_ca_states = QPushButton("Read CA states")
        self.read_ca_strategies = QPushButton("Read CA strategies")
        v_layout.addRow(self.read_ca_states)
        v_layout.addRow(self.read_ca_strategies)

    def start(self):
        pass

    def _create_parameters_layout(self):
        v_layout = QFormLayout()
        self.generalLayout.addLayout(v_layout)

        v_layout.addRow(QLabel("Simulation parameters"))

        self.n_rows = QLineEdit()
        v_layout.addRow(QLabel("(M+2) rows"), self.n_rows)

        self.n_cols = QLineEdit()
        v_layout.addRow(QLabel("(N+2) columns"), self.n_cols)

        self.p_init_c = QLineEdit()
        v_layout.addRow(QLabel("p_init_C"), self.p_init_c)

        self.sharing = QCheckBox()
        v_layout.addRow(QLabel("sharing"), self.sharing)

        v_layout.addRow(QLabel("Competition type"))
        self.btn_group = QButtonGroup()
        self.loc_prop_sel = QRadioButton()
        self.btn_group.addButton(self.loc_prop_sel)
        self.loc_tour = QRadioButton()
        self.btn_group.addButton(self.loc_tour)

        v_layout.addRow(QLabel("loc_prop_sel"), self.loc_prop_sel)
        v_layout.addRow(QLabel("loc_tour"), self.loc_tour)

        self.p_state_mut = QLineEdit()
        v_layout.addRow(QLabel("p_state_mut"), self.p_state_mut)

        self.p_strat_mut = QLineEdit()
        v_layout.addRow(QLabel("p_strat_mut"), self.p_strat_mut)

        self.if_seed = QCheckBox()
        self.if_seed.setText("seed")
        self.seed = QLineEdit()
        v_layout.addRow(self.if_seed, self.seed)

        self.num_of_iter = QLineEdit()
        v_layout.addRow(QLabel("num_of_iter"), self.num_of_iter)

        self.num_of_exper = QLineEdit()
        v_layout.addRow(QLabel("num_of_exper"), self.num_of_exper)

        v_layout.addRow(QLabel("payoff function"))

        grid = QGridLayout()
        v_layout.addRow(grid)
        grid.addWidget(QLabel("player"), 1,0)
        grid.addWidget(QLabel("D"), 2,0)
        grid.addWidget(QLabel("C"), 3,0)


        grid.addWidget(QLabel("neighbor"), 0,1)
        grid.addWidget(QLabel("D"), 1,1)
        grid.addWidget(QLabel("C"), 1,2)

        vl = QVBoxLayout()
        self.edit_a = QLineEdit()
        vl.addWidget(self.edit_a)
        self.edit_a1 = QLineEdit()
        vl.addWidget(self.edit_a1)
        grid.addLayout(vl, 2,1)

        vl = QVBoxLayout()
        self.edit_b = QLineEdit()
        vl.addWidget(self.edit_b)
        self.edit_b1 = QLineEdit()
        vl.addWidget(self.edit_b1)
        grid.addLayout(vl, 2,2)

        self.edit = QLineEdit()
        grid.addWidget(self.edit, 3,1)

        self.edit_c = QLineEdit()
        grid.addWidget(self.edit_c, 3,2)

        self.start_button = QPushButton("START")
        self.start_button.clicked.connect(self.start)
        grid.addWidget(self.start_button, 4, 2)






# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = PyCalcUi()
    view.show()
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()