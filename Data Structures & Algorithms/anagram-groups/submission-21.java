class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        /* the idea is to have a standard key defined for each string*/
        Map<String, List<String>> groups = new HashMap<>();

        for (String string : strs){
            char [] sort = string.toCharArray();
            Arrays.sort(sort);
            String key = new String(sort);
            groups.computeIfAbsent(key, k -> new ArrayList<>()).add(string );
        }
        return new ArrayList<>(groups.values());

    }
}
