class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length-1;

        while(true){
            int number = numbers[l] + numbers[r];
            if(number<target){
                l ++;
            }
            else if(number>target){
                r--;
            }
            else{
                return new int[] {l+1,r+1};
            }
        }
    }
}
