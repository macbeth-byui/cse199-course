#include<iostream>
#include<vector>

using namespace std;

double average(vector<int> &numbers) {
    double total = 0;
    for (int number : numbers) {
        total += number;
    }
    double avg = total / numbers.size();
    return avg;
}

int main() {
    vector<int> my_numbers = {3,1,6,3,5,4,6,2};
    double my_avg = average(my_numbers);
    cout << "Average = " << my_avg << endl;
    return 0;
}