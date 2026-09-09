class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> charCount = new HashMap<>();

        for(char c: s.toCharArray()){
            if(charCount.containsKey(c)){
                charCount.put(c, charCount.get(c) + 1);
            } else{
                charCount.put(c, 1);
            }
        }

        for(char c: t.toCharArray()){
            if (charCount.containsKey(c) == false || charCount.get(c) == 0)
                return false;
            
            charCount.put(c,charCount.get(c) - 1);
        }
    
        return true;
    }
}
