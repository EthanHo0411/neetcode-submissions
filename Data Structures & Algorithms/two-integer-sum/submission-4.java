class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> records = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int diff = target- num;
            if(records.containsKey(diff)){
                return new int[] {records.get(diff), i};
            }

            records.put(num, i);
        }
        return new int[] {};
    }
}
