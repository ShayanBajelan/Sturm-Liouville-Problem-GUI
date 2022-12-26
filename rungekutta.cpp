#include "rungekutta.h"
#include <iostream>
#include <math.h>

using namespace std;

Solver::LD Solver::p1;
Solver::LD Solver::p2;
Solver::LD Solver::p3;
Solver::LD Solver::q1;
Solver::LD Solver::q2;
Solver::LD Solver::q3;
Solver::LD Solver::w1;
Solver::LD Solver::w2;
Solver::LD Solver::w3;
Solver::LD Solver::theta0;

Solver::Solver() {}

Solver::LD Solver::dtheta_dx(LD x, LD theta, LD lambda, LD p_x, LD q_x, LD w_x)
{
    Solver::LD return_value = (lambda * w_x - q_x) * std::pow(std::sin(theta) , 2) + (1 / p_x) * std::pow(std::cos(theta) , 2);
    return return_value;
}

int Solver::calcN(LD a, LD b, LD h)
{
    return static_cast<int>((b - a) / h);
}

Solver::LD Solver::thetaDiff(int n, LD theta)
{
    return std::abs(static_cast<LD>(n) - theta / M_PI);
}

Solver::LD Solver::rungeKutta(LD a, LD b, LD h, LD theta0, LD lambda)
{
    auto n = calcN(a, b, h);
    auto theta = theta0;
    for (int i = 1; i < n + 1; i++) {
        auto k1 = h * dtheta_dx(a, theta, lambda, p1, q1, w1);
        auto k2 = h * dtheta_dx(a + 0.5 * h, theta + 0.5 * k1, lambda, p2, q2, w2);
        auto k3 = h * dtheta_dx(a + 0.5 * h, theta + 0.5 * k2, lambda, p2, q2, w2);
        auto k4 = h * dtheta_dx(a + h, theta + k3, lambda, p3, q3, w3);
        theta = theta + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4);
        a += h;
    } 
    return theta;
}

void Solver::setPx(LD p1, LD p2, LD p3)
{
    Solver::p1 = p1;
    Solver::p2 = p2;
    Solver::p3 = p3;
}

void Solver::setQx(LD q1, LD q2, LD q3)
{
    Solver::q1 = q1;
    Solver::q2 = q2;
    Solver::q3 = q3;
}

void Solver::setWx(LD w1, LD w2, LD w3)
{
    Solver::w1 = w1;
    Solver::w2 = w2;
    Solver::w3 = w3;
}

void Solver::setTheta0(LD theta0)
{
    Solver::theta0 = theta0;
}

Solver::LD Solver::solve(LD a, LD b, LD h, LD lambda_min, LD lambda_max, int n)
{
    static int counter = 0;
    auto lambda_mid = (lambda_max + lambda_min) / 2;
    auto theta = rungeKutta(a, b, h, theta0, lambda_mid);
    auto theta_min = rungeKutta(a, b, h, theta0, lambda_min);
    auto theta_max = rungeKutta(a, b, h, theta0, lambda_max);
    auto diff = thetaDiff(n, theta);
    auto diff_min = thetaDiff(n, theta_min);
    auto diff_max = thetaDiff(n, theta_max);
    std::cout << "attemp " << counter << " diff " << diff << " lmid " << lambda_mid << std::endl;
    counter++;
    if (diff < 1e-8) {
        return lambda_mid;
    }
    else {
        if (diff_min > diff_max) {
            lambda_min = lambda_mid;
        }
        else {
            lambda_max = lambda_mid;
        }
        return solve(a, b, h, lambda_min, lambda_max, n);
    }
}

void test()
{
    std::cout << "test";
}

long double test2(long double v)
{
    // Solver k();
    std::cout << "Arrkslnfn\n";
    return 10;
}

double test3(double v)
{
    std::cout << "test3";
    return v;
}

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
                  int n)
{
    std::cout << "starting to solve\n";
    Solver::setPx(p1, p2, p3);
    Solver::setQx(q1, q2, q3);
    Solver::setWx(w1, w2, w3);
    Solver::setTheta0(theta0);
    return Solver::solve(a, b, h, lambda_min, lambda_max, n);
}