#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int, int> m;

    for (int i = 0; i < nums.size(); i++) {
        int n = nums[i];

        if (m.count(n) && abs(i - m[n]) <= k) {
            return true;
        }

        m[n] = i;
    }

    return false;
}

int main() {
    int size;
    cin >> size;

    vector<int> nums(size);

    for (int i = 0; i < size; i++) {
        cin >> nums[i];
    }

    int k;
    cin >> k;

    if (containsNearbyDuplicate(nums, k))
        cout << "true";
    else
        cout << "false";

    return 0;
}