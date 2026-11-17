
class Solution {

    public boolean isAnagram(String s, String t) {
        Map<String, Integer> freq1 = new HashMap<>();
        Map<String, Integer> freq2 = new HashMap<>();
        List<String> s1 = List.of(s.split(""));
        List<String> t1 = List.of(t.split(""));
        for(String x: s1){
            freq1.put(x , freq1.getOrDefault(x,0)+1);
        }

        for(String x:t1){
            freq2.put(x,freq2.getOrDefault(x,0)+1);
        }
        return freq1.equals(freq2);
    }
}
