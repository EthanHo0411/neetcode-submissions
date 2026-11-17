class Solution {
    public int[] twoSum(int[] nums, int target) {

        /* guaranteed solutions implies the diff between the required pair will eventually be found*/
        /* store the*/
        Map<Integer, Integer> store = new HashMap<>();
        for (int i = 0 ; i < nums.length; i++){
            int number = nums[i];
            int diff = target - number; 
            if (store.containsKey(diff)){
                return new int [] {store.get(diff),i};
            } 
            store.put(number, i);
        }
        return new int [] {};
}
}