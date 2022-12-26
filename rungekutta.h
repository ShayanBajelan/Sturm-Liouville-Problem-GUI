#pragma once 

#include <iostream>
//#include "SymbolicC++/headers/symbolicc++.h"
#define _USE_MATH_DEFINES

class Solver {
    using LD = double;
    public:
        Solver();
        ~Solver() = default;
        static void setPx(LD p1, LD p2, LD p3);
        static void setQx(LD q1, LD q2, LD q3);
        static void setWx(LD w1, LD w2, LD w3);
        static void setTheta0(LD theta0);
        static LD solve(LD a, LD b, LD h, LD lambda_min, LD lambda_max, int n);
    private:
        static LD p1, p2, p3, q1, q2, q3, w1, w2, w3, theta0;
        static LD dtheta_dx(LD x, LD theta, LD lambda, LD p_x, LD q_x, LD w_x);
        static int calcN(LD a, LD b, LD h);
        static LD thetaDiff(int n, LD theta);
        static LD rungeKutta(LD a, LD b, LD h, LD theta0, LD lambda);
};

extern "C" {
    void test();
    long double test2(long double v);
    double test3(double v);
    
    double solve(double a,
                      double b,
                      double h,
                      double p1,
                      double p2,
                      double p3,
                      double q1,
                      double q2,
                      double q3,
                      double w1,
                      double w2,
                      double w3,
                      double theta0, 
                      double lambda_min,
                      double lambda_max,
                      int n);
}
