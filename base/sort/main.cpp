#include <iostream>
#include <vector>

using namespace std;

void mergeSortImpl(vector<int> &vec, size_t s, size_t e, vector<int> &tmp) {
    if (s < e) {
        size_t m = (s + e) / 2;
        mergeSortImpl(vec, s, m, tmp);
        mergeSortImpl(vec, m + 1, e, tmp);
        size_t i = s;
        size_t p = s, q = m + 1;
        while (p <= m || q <= e) {
            if (q > e || p <= m && vec[p] < vec[q])
                tmp[i++] = vec[p++];
            else
                tmp[i++] = vec[q++];
        }
        for (size_t i = s; i <= e; ++i)
            vec[i] = tmp[i];
    }
}

void MergeSort(vector<int> &vec) {
    vector<int> tmp(vec.size());
    mergeSortImpl(vec, 0, vec.size(), tmp);
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}