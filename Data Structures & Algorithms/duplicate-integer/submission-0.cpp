class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dup;
        for (int i : nums){
            if(dup.count(i)){
                return true;
            }
            else{
                dup.insert(i);
            }
        }
        return false;
    }
};