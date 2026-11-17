class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

    List<List<Integer>> result = new ArrayList<>();
    Arrays.sort(nums);
    int n = nums.length;
    for (int i = 0 ; i< n-2; i++){
        //make sure the start its a negative so that the equation is valid
        if (nums[i] > 0){break;}
        //skip the ones that is repeating
        if (i > 0 && nums[i] == nums[i-1]){continue;}

        int target = -nums[i];
        int j = i+1;
        int k = n-1;
        while (j<k){
            int total = nums[j]+nums[k];
            if (total > target ){ k-=1;}
            else if (total < target){ j+=1;}
            else { 
                result.add(Arrays.asList(nums[i], nums[j], nums[k]));
                j+=1;
                while (nums[j] == nums[j-1] && j<k){
                    j+=1;
                }
            }
        }
        
    }
    return result;
    }
}
