class Solution {
    public boolean isPowerOfThree(int n) {
        if(n==1) return true;
        if(n%3!=0 || n<=0) return false;
        else{
            return isPowerOfThree(n/3);
        }

    }
}