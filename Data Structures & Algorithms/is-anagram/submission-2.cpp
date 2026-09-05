class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())return false; 
        map<char, int>sCounter, tCounter; 
        for(int i = 0; i < s.size(); i++){
            sCounter[s[i]]++; tCounter[t[i]]++; 
        }
        for(int i = 0; i < s.size(); i++){
            if (sCounter[s[i]] != tCounter[s[i]])return false; 
        }
        return true; 
    }
};
