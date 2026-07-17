#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> n;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (i > k) {
                n.erase(nums[i - k - 1]);
            }
            
            if (n.count(nums[i])) {
                return true;
            }
            
            n.insert(nums[i]);
        }
        
        return false;
    }
};