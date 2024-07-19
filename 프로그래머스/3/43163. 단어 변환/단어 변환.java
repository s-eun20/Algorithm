import java.util.ArrayDeque;
import java.util.Queue;

public class Solution {
    public int solution(String begin,String target, String[] words) {
        Queue<WordState> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[words.length];

        queue.offer(new WordState(begin,0));
        
        
        while (!queue.isEmpty()) {
            // 방문
            WordState curr = queue.poll();
            // 방문한 곳이 내가 찾던 target이라면 return cnt
            if(curr.word.equals(target)) {
                return curr.cnt;
            }
            
            // nextvertex 예약
            for(int i=0; i<words.length; i++) {
                if(getDiffCount(curr.word,words[i])==1) {
                    if(!visited[i]) {
                        queue.offer(new WordState(words[i],curr.cnt+1));
                        visited[i]=true;
                    }
                }
            }
            
        }
        int answer = 0;
        return answer;
    }
    int getDiffCount(String word, String target) {
        int diffCount = 0;
        for(int i=0; i<word.length(); i++) {
            if(word.charAt(i)!=target.charAt(i)) diffCount++;
        }
        return diffCount;
    }
    class WordState {
        String word;
        int cnt;

        public WordState(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }
    }

}