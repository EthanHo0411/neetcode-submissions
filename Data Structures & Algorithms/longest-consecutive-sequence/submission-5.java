class Solution {
    public int longestConsecutive(int[] nums) {
        //firstly to determine the longest consecutive sequence, we need to identify the start of each seqeuence
        //the start of a sequence would only have right neighbour
        //first  store the numbers in hashset for O(1) checking for existence
        //then iterate through individual numbers and determine start of a sequence
        //increment the length of the sequence with each immediate right neighbour found
        //record the max length found so far
        //create a new hashmap
        Set<Integer> numbers = new HashSet();

        //store the numbers in the hashset
        for(int i = 0; i<nums.length; i++){
            numbers.add(nums[i]);
        }

        //store the max length
        int maxlength = 0;
        //iterate through each number and check if its start of sequence
        for(int i = 0; i< nums.length;i++){
            if(!numbers.contains(nums[i]-1)){
                int number = nums[i];
                int length = 0;
                while(numbers.contains(number)){
                    number++;
                    length ++ ;
                }
                if(length>maxlength){
                    maxlength = length;
                }
            }
        }
        return maxlength;
    }
}
