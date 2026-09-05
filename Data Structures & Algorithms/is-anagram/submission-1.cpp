class Solution {
public:
    bool isAnagram(string s, string t) {
        // Hashmap approach. 
        unordered_map<int, int> sMap, tMap; 
        int sLen = s.size(), tLen = t.size(); 
        if (sLen != tLen)
            return false; 
        for(int i = 0; i < sLen; i++)
            sMap[s[i]]++; 
        for(int j = 0; j < tLen; j++)
            tMap[t[j]]++; 
        for(int i = 0; i < sLen; i++){
            if (sMap[s[i]]!=tMap[s[i]])
                return false; 
        }
        return true;     
    }
};
