class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = nums.size();
        for(int i = 0; i < k; i++){
            if(nums[i] == val){
                nums.erase(nums.begin() + i);
                nums.push_back(val);
                i--;
                k--;
            }
        }
        return k;
    }
};