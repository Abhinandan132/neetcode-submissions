class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // Idea based on sorting string on lexical order. 
        int n = strs.size();
        if (n == 1)
            return strs[0]; 
        sort(strs.begin(), strs.end()); 
        string prefix = "", first = strs[0], last = strs[n - 1]; 
        int minLength = min(first.size(), last.size()); 
        for(int i = 0; i < minLength; i++){
            if (first[i] == last[i])
                prefix += first[i]; 
            else
                break; 
        }
        return prefix; 
    }
};