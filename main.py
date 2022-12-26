from PyQt5.QtWidgets import QApplication, QMainWindow
from Strum_Liouville_GUI import Ui_Sturm_Liouville
import sys
from Class_Sturm import SlP
import math
from sympy.parsing.mathematica import parse_mathematica
import solver


p_coefficient_str = ""
q_coefficient_str = ""
w_coefficient_str = ""
int_a = None
int_b = None
int_n = None
Sturm_Liouville_object = SlP()
h = 0.000001

class Introwindow(QMainWindow, Ui_Sturm_Liouville):
    def __init__(self, parent=None):
        super(Introwindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle("Approximated Eigenvalues of the Strum-Liouville problem")
        #class functions
        self.pushButton.clicked.connect(self.applied_p_coefficient)
        self.pushButton_2.clicked.connect(self.applied_q_coefficient)
        self.pushButton_3.clicked.connect(self.applied_w_coefficient)
        self.pushButton_4.clicked.connect(self.applied_a_number)
        self.pushButton_5.clicked.connect(self.applied_b_number)
        self.pushButton_6.clicked.connect(self.applied_n_number)
        self.pushButton_8.clicked.connect(self.cancel_button_pressed)
        self.pushButton_7.clicked.connect(self.generate_button_pressed)
        self.pushButton_9.clicked.connect(self.clear_button_pressed)
        self.pushButton_7.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        self.textEdit.setReadOnly(True)
        
        #class variables
        self.check_genrate_for_p = False
        self.check_genrate_for_q = False
        self.check_genrate_for_w = False
        self.check_genrate_for_a = False
        self.check_genrate_for_b = False
        self.check_genrate_for_n = False
        
        
    def applied_p_coefficient(self):
        global p_coefficient_str
        p_coefficient_str = self.lineEdit.text()
        if p_coefficient_str != "":
            self.lineEdit.setReadOnly(True)
            self.pushButton.setEnabled(False)
            self.check_genrate_for_p = True
        print(p_coefficient_str)
        
        if (self.check_genrate_for_p == True and
            self.check_genrate_for_q == True and
            self.check_genrate_for_w == True and
            self.check_genrate_for_a == True and
            self.check_genrate_for_b == True and
            self.check_genrate_for_n == True):
            
            self.pushButton_7.setEnabled(True)
        

    def applied_q_coefficient(self):
        global q_coefficient_str
        q_coefficient_str = self.lineEdit_2.text()
        if q_coefficient_str != "":
            self.lineEdit_2.setReadOnly(True)
            self.pushButton_2.setEnabled(False)
            self.check_genrate_for_q = True
        print(q_coefficient_str)
        
        if (self.check_genrate_for_p == True and
            self.check_genrate_for_q == True and
            self.check_genrate_for_w == True and
            self.check_genrate_for_a == True and
            self.check_genrate_for_b == True and
            self.check_genrate_for_n == True):
            
            self.pushButton_7.setEnabled(True)

    
    def applied_w_coefficient(self):
        global w_coefficient_str
        w_coefficient_str = self.lineEdit_3.text()
        if w_coefficient_str != "":
            self.lineEdit_3.setReadOnly(True)
            self.pushButton_3.setEnabled(False)
            self.check_genrate_for_w = True
        print(w_coefficient_str)
        
        if (self.check_genrate_for_p == True and
            self.check_genrate_for_q == True and
            self.check_genrate_for_w == True and
            self.check_genrate_for_a == True and
            self.check_genrate_for_b == True and
            self.check_genrate_for_n == True):
            
            self.pushButton_7.setEnabled(True)

        
    def applied_a_number(self):
        if self.lineEdit_6.text() != "":
            global int_a
            int_a = math.modf(float(self.lineEdit_6.text()))[1]
            self.lineEdit_6.setReadOnly(True)
            self.pushButton_4.setEnabled(False)
            self.check_genrate_for_a = True
            print(int_a)        
        
        if (self.check_genrate_for_p == True and
            self.check_genrate_for_q == True and
            self.check_genrate_for_w == True and
            self.check_genrate_for_a == True and
            self.check_genrate_for_b == True and
            self.check_genrate_for_n == True):
            
            self.pushButton_7.setEnabled(True)

        
    def applied_b_number(self):
        if self.lineEdit_4.text() != "":    
            global int_b
            int_b_check = math.modf(float(self.lineEdit_4.text()))
            if int_b_check[0] == 0:
                int_b = int_b_check[1]
            else:
                int_b = int_b_check[1] + 1
            self.lineEdit_4.setReadOnly(True)
            self.pushButton_5.setEnabled(False)
            self.check_genrate_for_b = True
            print(int_b)
        
        if (self.check_genrate_for_p == True and
            self.check_genrate_for_q == True and
            self.check_genrate_for_w == True and
            self.check_genrate_for_a == True and
            self.check_genrate_for_b == True and
            self.check_genrate_for_n == True):
            
            self.pushButton_7.setEnabled(True)

        
    def applied_n_number(self):
        if self.lineEdit_5.text() != "":
            global int_n
            int_n = math.modf(float(self.lineEdit_5.text()))[1]
            self.lineEdit_5.setReadOnly(True)
            self.pushButton_6.setEnabled(False)
            self.check_genrate_for_n = True
            print(int_n)
            
        if (self.check_genrate_for_p == True and
            self.check_genrate_for_q == True and
            self.check_genrate_for_w == True and
            self.check_genrate_for_a == True and
            self.check_genrate_for_b == True and
            self.check_genrate_for_n == True):
            
            self.pushButton_7.setEnabled(True)

        
    def cancel_button_pressed(self):
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_6.setReadOnly(False)
        
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_5.setEnabled(True)
        self.pushButton_6.setEnabled(True)
        
        self.check_genrate_for_p = False
        self.check_genrate_for_q = False
        self.check_genrate_for_w = False
        self.check_genrate_for_a = False
        self.check_genrate_for_b = False
        self.check_genrate_for_n = False
        
        p_coefficient_str = ""
        q_coefficient_str = ""
        w_coefficient_str = ""
        int_a = None
        int_b = None
        int_n = None

        self.pushButton_7.setEnabled(False)
        self.pushButton_9.setEnabled(False)
        
    def generate_button_pressed(self):
        self.pushButton_7.setEnabled(False)
        Sturm_Liouville_object.eigenvalu_index_setter_n_UI(int_n)
        Sturm_Liouville_object.p_coefficient_setter_UI(p_coefficient_str)
        Sturm_Liouville_object.q_coefficient_setter_UI(q_coefficient_str)
        Sturm_Liouville_object.w_coefficient_setter_UI(w_coefficient_str)
        
        Sturm_Liouville_object.first_interval_value_setter_a_UI(int_a)
        Sturm_Liouville_object.last_interval_value_setter_b_UI(int_b)
        
        a = Sturm_Liouville_object.first_interval_value_getter_a()
        b = Sturm_Liouville_object.last_interval_value_getter_b()
        n = int(Sturm_Liouville_object.eigenvalu_index_getter_n())
        
        res = solver.solve(a,
                           b,
                           h,
                           Sturm_Liouville_object.p(a),
                           Sturm_Liouville_object.p(a + 0.5 * h),
                           Sturm_Liouville_object.p(a + h),
                           Sturm_Liouville_object.q(a),
                           Sturm_Liouville_object.q(a + 0.5 * h),
                           Sturm_Liouville_object.q(a + h),
                           Sturm_Liouville_object.w(a),
                           Sturm_Liouville_object.w(a + 0.5 * h),
                           Sturm_Liouville_object.w(a + h),
                           0,
                           Sturm_Liouville_object.lowerBand(n),
                           Sturm_Liouville_object.upperBand(n),
                           n)
        
        if (Sturm_Liouville_object.check_a_is_zero):
            self.textEdit.setPlainText(f"Approximation of {int(int_n)}'n eigenvalue is: {res}")
        else:
            self.textEdit.setPlainText(f"Approximation of {int(int_n)}'n eigenvalue is: {res/2}")
        
        self.pushButton_9.setEnabled(True)

    
    def clear_button_pressed(self):
        self.pushButton_9.setEnabled(False)
        self.textEdit.clear()
        self.pushButton_7.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Introwindow()
    w.show()
    sys.exit(app.exec_())