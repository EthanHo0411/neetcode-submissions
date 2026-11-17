
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> sets = new HashSet<>();
        for(int i = 0 ; i < nums.length; i++){
            if(sets.contains(nums[i])){
                return true;
            }
            sets.add(nums[i]);
        }
        return false;
    }
}
