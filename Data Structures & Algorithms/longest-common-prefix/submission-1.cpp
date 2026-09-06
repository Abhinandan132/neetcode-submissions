class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        // Naive implementation. T.C O(n * m)
        // string prefix = strs[0]; 
        // for(int i = 1; i < strs.size(); i++){
        //     int j = 0; 
        //     while(j < min(prefix.length(), strs[i].length())){
        //         if (prefix[j] != strs[i][j])
        //             break; 
        //         j++; 
        //     }
        //     prefix = prefix.substr(0, j); 
        // }
        // return prefix; 
        if (strs.size() == 1)return strs[0]; 
        sort(strs.begin(), strs.end()); 
        for(int i = 0; i < min(strs[0].length(), strs.back().length()); i++){
            if (strs[0][i] != strs.back()[i])return strs[0].substr(0, i); 
        }
        return strs[0]; 
    }
};