class Solution {
    public boolean isPerfectSquare(int num) {
        return binarySearch(num, 1, num);
    }

    private boolean binarySearch(int num, long low, long high) {
        if (low > high) return false;
        long mid = low + (high - low) / 2;
        long square = mid * mid;
        if (square == num) return true;
        else if (square < num) return binarySearch(num, mid + 1, high);
        else return binarySearch(num, low, mid - 1);
    }
}