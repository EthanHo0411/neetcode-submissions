class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dictt = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int num = nums[i];
            int remain = target - num;
            if (dictt.containsKey(remain)){
                return new int[] {dictt.get(remain), i};
            }
            dictt.put(num, i);
        }
        return new int[] {};
    }
}
