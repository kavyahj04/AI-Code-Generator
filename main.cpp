
#include <iostream>
#include <iomanip>
#include <chrono>
int main() {
    auto start = std::chrono::high_resolution_clock::now();
    double result = 1.0;
    const int iterations = 200000000;
    const double param1 = 4.0;
    const double param2 = 1.0;
    for(int i = 1; i <= iterations; ++i) {
        double j = i * param1 - param2;
        result -= 1.0 / j;
        j = i * param1 + param2;
        result += 1.0 / j;
    }
    result *= 4.0;
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;
    std::cout << std::fixed << std::setprecision(12) << "Result: " << result << '\n';
    std::cout << std::fixed << std::setprecision(6) << "Execution Time: " << elapsed.count() << " seconds\n";
}
