class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for(int n : nums){
            set.add(n);
        }
        int prevMax = 0;
        for(int n : set){
            int max = 0;
            if(!set.contains(n-1)){
            
            while (set.contains(n+1)){
                max++;
                n++;
            }
            max++;
            prevMax = Math.max(max, prevMax);
        }
        }
        return prevMax;
    }
}
