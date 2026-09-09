class Solution {
    public int[] countBits(int n) {
        int[] countedBits = new int[n+1];

        for(int i=0; i<(n+1); i++){
            System.out.printf("%d",i);
            countedBits[i] = Integer.bitCount(i);
        }

        return countedBits;
    }
}
