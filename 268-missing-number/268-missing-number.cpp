class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // int sum = 0;
        // long n = nums.size();
        // for(int i = 0 ; i< n ; i++ ){
        //     sum += nums[i];
        // }   
        // return n*(n+1)/2-sum;  
        long n = nums.size();
        return n*(n+1)/2-accumulate(begin(nums), end(nums), 0);
    }
    
    
};