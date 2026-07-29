class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        int count[26] = {0};
        for(int i = 0 ; i < s.length() ; ++i){
            count[s[i]-'a']++; // incresing count of string one;
            count[t[i]-'a']--; // decresing count fo string two;
        }
        for(int i = 0 ; i < 26 ; ++i){
            if(count[i] != 0) return false;
        }
        return true;
    }
};
