class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> group = new HashMap<>();
        for (int i = 0; i< strs.length;i++){
            String s = strs[i];
            char [] temp = s.toCharArray();
            Arrays.sort(temp);
            String key = new String(temp);
            group.computeIfAbsent(key, k-> new ArrayList<>()).add(s);
        } 
        return new ArrayList<>(group.values());
    }
}
