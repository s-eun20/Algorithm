public class Solution {
    int answer = -1;
    public int solution(int k,int[][] dungeons) {
        
        int n = dungeons.length;
        boolean[] visited =  new boolean[n];
        backtrack(visited,n,k,dungeons,0);
        return answer;
    }

    public void backtrack(boolean[] visited, int n,int k, int[][] dungeons, int cnt) {
        if(cnt > answer) {
            answer = cnt;
        }
        //recursive call
        for(int i=0; i<n; i++) {
            if(k >= dungeons[i][0] && !visited[i]) {
                visited[i] = true;
                backtrack(visited,n,k-dungeons[i][1],dungeons,cnt+1);
                visited[i]=false;
            }
        }
    }
}
