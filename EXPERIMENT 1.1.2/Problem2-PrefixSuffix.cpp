#include <iostream>
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n);

    //Prefix Pass
    int pre = 1;
    for(int i=0; i<n; i++){
        res[i] = pre;
        pre *= nums[i];
    }
    // Suffix Pass
    int suf = 1;
    for(int i =n-1; i>=0; i--){
        res[i] *= suf;
        suf *= nums[i];
    }
    
    return res;
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    vector<int> ans = productExceptSelf(nums);

    cout << "Output: ";
    for (int i = 0; i < n; i++) {
        cout << ans[i] << " ";
    }

    cout << endl;

    return 0;
}