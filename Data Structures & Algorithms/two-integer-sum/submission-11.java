class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dictt = new HashMap<>();
        for (int i = 0; i<nums.length; i++){
            int num = nums[i];
            int diff = target - num;
            if (dictt.containsKey(diff)){
                return new int [] {dictt.get(diff), i};
            }
            dictt.put(num, i);
        }
        return new int[] {};
    }
}
