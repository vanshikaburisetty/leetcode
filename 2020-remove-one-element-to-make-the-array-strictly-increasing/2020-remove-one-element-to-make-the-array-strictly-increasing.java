class Solution {
    public boolean canBeIncreasing(final int[] nums) {
        int count = 0;
        int idx = 0;

        for(int i = 1; i < nums.length; i++){
            if(nums[i - 1] >= nums[i]){
                count++;
                idx = i - 1;
            }
        }

        if(count > 1)
           return false;

        if(idx == 0 || idx == nums.length - 2)
            return true;

        if(nums[idx + 1] > nums[idx - 1] || nums[idx + 2] > nums[idx])
            return true;

        return false;
    }
}