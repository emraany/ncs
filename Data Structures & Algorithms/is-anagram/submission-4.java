class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sSet = new HashMap<>();
        HashMap<Character, Integer> tSet = new HashMap<>();

        for (char c : s.toCharArray())
            sSet.put(c, sSet.getOrDefault(c, 0) + 1);

        for (char c : t.toCharArray())
            tSet.put(c, tSet.getOrDefault(c, 0) + 1);

        return sSet.equals(tSet);
    }
}
