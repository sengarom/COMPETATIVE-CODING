#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_set<int> s;

    for (int i = 0; i < nums.size(); i++) {
        if (i > k) {
            s.erase(nums[i - k - 1]);
        }

        if (s.count(nums[i])) {
            return true;
        }

        s.insert(nums[i]);
    }

    return false;
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
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