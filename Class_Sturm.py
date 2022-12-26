# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 01:38:12 2022

@author: aasus
"""

import sympy
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy.abc import x
from scipy.integrate import quad
import math
import solver
from sympy.parsing.mathematica import parse_mathematica

sympy.init_printing(pretty_print=True)

class SlP:
    def __init__(self):
        #Private variables
        self.__p_coefficient = None
        self.__q_coefficient = None
        self.__w_coefficient = None
        self.__a = None
        self.__b = None 
        self.__n = None
        self.__p_coefficient_string = None 
        self.__q_coefficient_string = None 
        self.__w_coefficient_string = None 
        #Public variables
        self.interval_List=[]
        self.check_a_is_zero = True
        
    
    def p_coefficient_setter_UI(self, p_coefficient_str):
        self.__p_coefficient_string = p_coefficient_str
        for i in range(0, len(self.__p_coefficient_string)):
            if self.__p_coefficient_string[i] == 'e':
                self.__p_coefficient_string = self.__p_coefficient_string.replace(self.__p_coefficient_string[i], "2.718281828459045")
        self.__p_coefficient = parse_mathematica(self.__p_coefficient_string)
    
    def q_coefficient_setter_UI(self, q_coefficient_str):
        self.__q_coefficient_string = q_coefficient_str
        for i in range(0, len(self.__q_coefficient_string)):
            if self.__q_coefficient_string[i] == 'e':
                self.__q_coefficient_string = self.__q_coefficient_string.replace(self.__q_coefficient_string[i], "2.718281828459045")
        self.__q_coefficient = parse_mathematica(self.__q_coefficient_string)
        
    def w_coefficient_setter_UI(self, w_coefficient_str):
        self.__w_coefficient_string = w_coefficient_str
        for i in range(0, len(self.__w_coefficient_string)):
            if self.__w_coefficient_string[i] == 'e':
                self.__w_coefficient_string = self.__w_coefficient_string.replace(self.__w_coefficient_string[i], "2.718281828459045")
        self.__w_coefficient = parse_mathematica(self.__w_coefficient_string)

   
    def p_coefficient_getter(self):
        return self.__p_coefficient
    
    def p_coefficient_string_getter(self):
        return self.__p_coefficient_string
    
    def p_coefficient_setter(self):
        self.__p_coefficient_string = input("Enter p(x): ")
        for i in range(0, len(self.__p_coefficient_string)):
            if self.__p_coefficient_string[i] == 'e':
                self.__p_coefficient_string = self.__p_coefficient_string.replace(self.__p_coefficient_string[i], "2.718281828459045")
        self.__p_coefficient = parse_mathematica(self.__p_coefficient_string)
        
    
    def q_coefficient_getter(self):
        return self.__q_coefficient
    
    def q_coefficient_string_getter(self):
        return self.__q_coefficient_string
    
    
    def q_coefficient_setter(self):
        self.__q_coefficient_string = input("Enter q(x): ")
        for i in range(0, len(self.__q_coefficient_string)):
            if self.__q_coefficient_string[i] == 'e':
                self.__q_coefficient_string = self.__q_coefficient_string.replace(self.__q_coefficient_string[i], "2.718281828459045")
        self.__q_coefficient = parse_mathematica(self.__q_coefficient_string)
        
    
    def w_coefficient_getter(self):
        return self.__w_coefficient
    
    def w_coefficient_string_getter(self):
        return self.__w_coefficient_string
    
    def w_coefficient_setter(self):
        self.__w_coefficient_string = input("Enter w(x): ")
        for i in range(0, len(self.__w_coefficient_string)):
            if self.__w_coefficient_string[i] == 'e':
                self.__w_coefficient_string = self.__w_coefficient_string.replace(self.__w_coefficient_string[i], "2.718281828459045")
        self.__w_coefficient = parse_mathematica(self.__w_coefficient_string)
        
    
    def first_interval_value_getter_a(self):
        int_a = math.modf(self.__a)[1]
        return (int_a)
    
    
    def first_interval_value_setter_a(self):
        self.__a = float(input("First Interval Value a: "))
        if(self.__a != 0):
            self.check_a_is_zero = False  
            
    def first_interval_value_setter_a_UI(self, int_a):
            self.__a = int_a
            if(self.__a != 0):
                self.check_a_is_zero = False
                                
    def first_interval_value_setter_a_backedn(self, a):
        self.__a = sympy.Integer(a)
    
    
    def last_interval_value_getter_b(self):
        int_b = math.modf(self.__b)[1]
        return int_b        
    
    def last_interval_value_setter_b(self):
        self.__b = float(input("Last Interval Value b: "))
        if self.first_interval_value_getter_a() != None and self.last_interval_value_getter_b() != None:
            self.create_interval_list_between_a_and_b(self.first_interval_value_getter_a(), self.last_interval_value_getter_b())
            
    def last_interval_value_setter_b_UI(self, int_b):
        self.__b = int_b
        if self.first_interval_value_getter_a() != None and self.last_interval_value_getter_b() != None:
            self.create_interval_list_between_a_and_b(self.first_interval_value_getter_a(), self.last_interval_value_getter_b())
 
    
    def last_interval_value_setter_b_backend(self, b):
        self.__b = sympy.Integer(b)
        
    
    def eigenvalu_index_getter_n(self):
        return self.__n
    
    
    def eigenvalu_index_setter_n(self):
        self.__n = parse_expr(input("n'th eigenvalue number: "))
        
    def eigenvalu_index_setter_n_UI(self, int_n):
        self.__n = int_n
    
    
    def p(self, x_val):
        if(self.check_a_is_zero):
            return sympy.lambdify(x, self.p_coefficient_getter(), 'numpy')(x_val)
        else:
            return (sympy.lambdify(x, self.p_coefficient_getter().subs({x : (x * (self.last_interval_value_getter_b() - self.first_interval_value_getter_a()) + self.first_interval_value_getter_a())}), 'numpy')(x_val)) / (self.last_interval_value_getter_b() - self.first_interval_value_getter_a())

    
    def q(self, x_val):
        if(self.check_a_is_zero):
            return sympy.lambdify(x, self.q_coefficient_getter(), 'numpy')(x_val)
        else:
            return sympy.lambdify(x, self.q_coefficient_getter().subs({x : (x * (self.last_interval_value_getter_b() - self.first_interval_value_getter_a()) + self.first_interval_value_getter_a())}), 'numpy')(x_val)

    
    def w(self, x_val):
        if(self.check_a_is_zero):
            return sympy.lambdify(x, self.w_coefficient_getter(), 'numpy')(x_val)
        else:
            return sympy.lambdify(x, self.w_coefficient_getter().subs({x : (x * (self.last_interval_value_getter_b() - self.first_interval_value_getter_a()) + self.first_interval_value_getter_a())}), 'numpy')(x_val)        
    
    
    def create_interval_list_between_a_and_b(self, a, b):
        if a == b:
            while(True):
                print("\nPlease set different a and b")
                self.first_interval_value_setter_a()
                self.last_interval_value_setter_b()
                if self.first_interval_value_getter_a() != self.last_interval_value_getter_b():
                    break
                
        self.first_interval_value_setter_a_backedn(sympy.Integer(a))
        self.last_interval_value_setter_b_backend(sympy.Integer(b))
        self.interval_List = np.arange(self.first_interval_value_getter_a(), self.last_interval_value_getter_b(), 0.01)
        
    
    def check_p_is_positive(self):
        check_pos = True
        for x_val in self.interval_List:
            if self.p(x_val)<0:
                check_pos = False
        if(check_pos):
            return True
        else:
            return False
       
    
    def find_c(self):
        if self.p_coefficient_getter() == None:
            self.p_coefficient_setter()
        if self.w_coefficient_getter() == None:
            self.w_coefficient_setter()
        if len(self.interval_List) == 0:
            self.first_interval_value_setter_a()
            self.last_interval_value_setter_b()
            self.create_interval_list_between_a_and_b(self.first_interval_value_getter_a(), self.last_interval_value_getter_b())
        list_mult = []
        if(self.check_p_is_positive()):
            for x_val in self.interval_List:
                list_mult.append(self.p(x_val) * self.w(x_val))
        else:
            print("\nCheck p(x) should be positive in [a, b]!")
            return None
        return max(list_mult)
        
    
    def find_m(self):
        if self.q_coefficient_getter() == None:
            self.q_coefficient_setter()
        if self.w_coefficient_getter() == None:
            self.w_coefficient_setter()
        if len(self.interval_List) == 0:
            self.first_interval_value_setter_a()
            self.last_interval_value_setter_b()
            self.create_interval_list_between_a_and_b(self.first_interval_value_getter_a(), self.last_interval_value_getter_b())
        if self.q(x) == 0:
            return 0
        else:
            list_div = []
            for x_val in self.interval_List:
                list_div.append((self.q(x_val)) / (self.w(x_val)))
            return min(list_div)
        
    
    def lowerBand(self, n):
        self.__n = n
        a = self.first_interval_value_getter_a()
        b = self.last_interval_value_getter_b()
        if (self.special_mode_ckeck()):
            return (4 * self.__n ** 2 ) / ((self.last_interval_value_getter_b() - self.first_interval_value_getter_a()) * quad(self.w, a, b)[0])
        else:
            return ((self.__n ** 2) * (float(sympy.pi ** 2))) / (self.find_c() * (float((quad(self.f, a, b))[0]) ** 2)) + self.find_m()
        
    
    def find_captal_c(self):
        if self.p_coefficient_getter() == None:
            self.p_coefficient_setter()
        if self.w_coefficient_getter() == None:
            self.w_coefficient_setter()
        if len(self.interval_List) == 0:
            self.first_interval_value_setter_a()
            self.last_interval_value_setter_b()
            self.create_interval_list_between_a_and_b(self.first_interval_value_getter_a(), self.last_interval_value_getter_b())
        list_mult = []
        if(self.check_p_is_positive()):
            for x_val in self.interval_List:
                list_mult.append(self.p(x_val) * self.w(x_val))
        else:
            print("\nCheck p(x) should be positive in [a, b]!")
            return None
        return min(list_mult)        
        

    def find_captal_m(self):
        if self.q_coefficient_getter() == None:
            self.q_coefficient_setter()
        if self.w_coefficient_getter() == None:
            self.w_coefficient_setter()
        if len(self.interval_List) == 0:
            self.first_interval_value_setter_a()
            self.last_interval_value_setter_b()
            self.create_interval_list_between_a_and_b(self.first_interval_value_getter_a(), self.last_interval_value_getter_b())
        if self.q(x) == 0:
            return 0
        else:
            list_div = []
            for x_val in self.interval_List:
                list_div.append(self.q(x_val) / (self.w(x_val)))
            return max(list_div)
    
    def f(self, x):
        return 1/self.p(x)
    
    def H(self):
        list_w_x = []
        for x_val in self.interval_List:
            list_w_x.append(self.w(x_val))
        return max(list_w_x)
    
    def upperBand(self, n):
        self.__n = n
        a = self.first_interval_value_getter_a()
        b = self.last_interval_value_getter_b()
        if (self.special_mode_ckeck()):
            return ((float(sympy.pi ** 2)) * (self.H()) * (self.__n ** 2)) / (float(quad(self.w, a, b,)[0])**2)
        else:
            return ((self.__n ** 2) * (float(sympy.pi ** 2))) / (self.find_captal_c() * (float((quad(self.f, a, b))[0]) ** 2)) + self.find_captal_m()
    
    
    def midPoint_calculation(self, a, b):
        return (a+b)/2
    
    
    def dtheta_dx(self, x, theta, lamda):
        return (lamda*self.w(x) - self.q(x))*(sympy.sin(theta)**2) + (1/self.p(x))*((sympy.cos(theta)) ** 2)
        
    
    def rungeKutta(self, a, theta0, b, h, lamda_val):
        n = int((b - a)/h)
        theta = theta0
        for i in range(1, n+1):
            k1 = h * self.dtheta_dx(a, theta, lamda_val)
            k2 = h * self.dtheta_dx(a + 0.5 * h, theta + 0.5 * k1, lamda_val)
            k3 = h * self.dtheta_dx(a + 0.5 * h, theta + 0.5 * k2, lamda_val)
            k4 = h * self.dtheta_dx(a + h, theta + k3, lamda_val)            
            theta = theta + (1.0 / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
            a = a + h
        return theta
    
    
    def solve(self, n):
        print("Here part 1")
        # b1 = self.lowerBand(self.eigenvalu_index_getter_n())
        # b2 = self.upperBand(self.eigenvalu_index_getter_n())
        b1 = self.lowerBand(n)
        print("b1: ", b1)
        b2 = self.upperBand(n)
        print("b2: ", b2)
        bM = self.midPoint_calculation(b1, b2)
        print("bM: ", bM)
        print("Here part 2")
        theta_b1 = self.rungeKutta(self.first_interval_value_getter_a(), 0, self.last_interval_value_getter_b(), 0.0001, b1)/math.pi
        theta_b2 = self.rungeKutta(self.first_interval_value_getter_a(), 0, self.last_interval_value_getter_b(), 0.0001, b2)/math.pi
        theta_bM = self.rungeKutta(self.first_interval_value_getter_a(), 0, self.last_interval_value_getter_b(), 0.0001, bM)/math.pi
        theta_b_answer = self.rungeKutta(self.first_interval_value_getter_a(), 0, self.last_interval_value_getter_b(), 0.0001, 83.1691538208952815)/math.pi
        # while(abs(self.eigenvalu_index_getter_n() - theta_bM / sympy.pi) > 0.1):
        #     if abs(self.eigenvalu_index_getter_n() - theta_b1 / sympy.pi) > abs(self.eigenvalu_index_getter_n() - theta_bM / sympy.pi):
                
        return [theta_b1, theta_bM, theta_b2, theta_b_answer]
    
    
    def special_mode_ckeck(self):
        if (self.p(x) == 1 and self.q(x) == 0):
            # print("Special func")
            return True
        else:
            # print("Ordinary func")
            return False
        
if __name__ == '__main__':
    sturm_liouville_problem_object = SlP()
    # sturm_liouville_problem_object.eigenvalu_index_setter_n()
    
    # sturm_liouville_problem_object.p_coefficient_setter_UI("e^x")
    # print(sturm_liouville_problem_object.p_coefficient_getter())
    
    sturm_liouville_problem_object.p_coefficient_setter()
    sturm_liouville_problem_object.q_coefficient_setter()
    sturm_liouville_problem_object.w_coefficient_setter()
    sturm_liouville_problem_object.first_interval_value_setter_a()
    sturm_liouville_problem_object.last_interval_value_setter_b()
    
    # list_upper_lower_lamda_1 = [sturm_liouville_problem_object.lowerBand(1), sturm_liouville_problem_object.upperBand(1)]
    # print(list_upper_lower_lamda_1)
    # list_upper_lower_lamda_2 = [sturm_liouville_problem_object.lowerBand(2), sturm_liouville_problem_object.upperBand(2)]
    # list_upper_lower_lamda_3 = [sturm_liouville_problem_object.lowerBand(3), sturm_liouville_problem_object.upperBand(3)]
    # list_upper_lower_lamda_4 = [sturm_liouville_problem_object.lowerBand(4), sturm_liouville_problem_object.upperBand(4)]
    list_upper_lower_lamda_3 = [sturm_liouville_problem_object.lowerBand(3), sturm_liouville_problem_object.upperBand(3)]
    print(list_upper_lower_lamda_3)
    
    a = sturm_liouville_problem_object.first_interval_value_getter_a()
    b = sturm_liouville_problem_object.last_interval_value_getter_b()

    # h = 0.000001
    # res = solver.solve( a,
    #                     b,
    #                     h,
    #                     sturm_liouville_problem_object.p(a),
    #                     sturm_liouville_problem_object.p(a + 0.5 * h),
    #                     sturm_liouville_problem_object.p(a + h),
    #                     sturm_liouville_problem_object.q(a),
    #                     sturm_liouville_problem_object.q(a + 0.5 * h),
    #                     sturm_liouville_problem_object.q(a + h),
    #                     sturm_liouville_problem_object.w(a),
    #                     sturm_liouville_problem_object.w(a + 0.5 * h),
    #                     sturm_liouville_problem_object.w(a + h),
    #                     0,
    #                     sturm_liouville_problem_object.lowerBand(7),
    #                     sturm_liouville_problem_object.upperBand(7),
    #                     7)
    # if (sturm_liouville_problem_object.check_a_is_zero):
    #         print("result: ", res)
    # else:
    #         print("result: ", res / 2)
    # print(sturm_liouville_problem_object.solve(2))
    