class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> sett =  new HashSet<>();
        for (int num : nums){
            if (sett.contains(num)){
                return true;
            }
            sett.add(num);
        }
        return false;
    }
}