class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character, Integer> sSet = new HashMap<>();
        HashMap <Character, Integer> tSet = new HashMap<>();
        for (char sC : s.toCharArray()){
            sSet.put(sC, sSet.getOrDefault(sC, 0) + 1);
        }
        for (char tC : t.toCharArray()){
            tSet.put(tC, tSet.getOrDefault(tC, 0) + 1);
        }

        if(sSet.equals(tSet)){
            return true;
        }
        return false;
    }
}
