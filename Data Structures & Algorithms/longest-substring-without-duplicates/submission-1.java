class Solution {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        Set<Character> check = new HashSet<>();
        int l = 0;

        for(int r = 0; r < s.length(); r++){
            while(check.contains(s.charAt(r))){
                check.remove(s.charAt(l));
                l++;
            }
            check.add(s.charAt(r));
            max = Math.max(max, r - l + 1);

        }

        

        return max;
    }
}
