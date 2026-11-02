public class Solution {
    public int MinimumPushes(string word) {
        int[] dp = new int[26];
        foreach (char c in word){
            dp[c-'a']++;
        }
        Array.Sort(dp);
        Array.Reverse(dp);
        int result = 0;
        int index = 8;
        for (int i=0;i<26;i++){
            if (dp[i]==0) continue;
            result += ((index/8) * dp[i]);
            index++;
        }
        return result;

    }
}