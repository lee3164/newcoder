#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void insert_heap(vector<int>& heap, int num, int size) {
        int i = size - 1;
        while (i > 0) {
            int j = (i - 1) / 2;
            if (heap[j] > num)
                break;
            heap[i] = heap[j];
            i = j;
        }
        heap[i] = num;
    }

    void build_heap(vector<int>& heap, int size) {
        int num = heap[0];
        int i =  0;
        while (i <= (size / 2 - 1))
        {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int max = left;
            if (right < size && heap[right] > heap[left])
                max = right;
            if (heap[max] > num) {
                heap[i] = heap[max];
                i = max;
            }
            else {
                break;
            }
        }
        heap[i] = num;
    }

    void heap_sort(vector<int>& heap) {
        auto size = heap.size();
        while (size > 0) {
            swap(heap[size-1], heap[0]);
            build_heap(heap, --size);
        }
    }

    vector<int> solution1(const vector<int>& input, int k) {
        vector<int> heap(k);
        int heap_size = 0;
        for (auto& num: input) {
            if (heap_size < k) {
                insert_heap(heap, num, ++heap_size);
            } else if (heap[0] > num) {
                heap[0] = num;
                build_heap(heap, heap.size());
            } else {
                continue;
            }
        }
        heap_sort(heap);
        return heap;
    }

    vector<int> solution2(vector<int> &input, int k) {
        // 利用冒泡排序，不过外层只用循环k次，时间复杂度O(nk)，这个答案也不错
        vector<int> res;
        if (k > input.size())
            return res;

        for (int i = 0; i < k; ++i) {
            int min = input.size() - 1;
            for (int j = min - 1; j >= i; --j) {
                if (input[min] > input[j])
                    min = j;
            }
            res.push_back(input[min]);
            swap(input[i], input[min]);
        }
        return res;
    }

    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        return solution2(input, k);
    }
};

int main()
{
    auto nums = Solution().GetLeastNumbers_Solution({69, 33, 91, 53, 46, 60, 96, 7, 24, 2}, 5);
    for (auto &num: nums) {
        cout << num << endl;
    }
    return 0;
}
