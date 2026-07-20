#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); ++i) {
            int n = nums[i];
            if (m.count(n) && abs(i - m[n]) <= k) {
                return true;
            }
            m[n] = i;
        }
        return false;
    }
};