import java.util.*;
class Solution {
    ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
    public int solution(int n, int[][] edge) {
        for(int i=0; i<=n; i++) graph.add(new ArrayList<>());
        
        for(int[] i : edge) {
            int v = i[0];
            int w = i[1];
            graph.get(v).add(w);
            graph.get(w).add(v);
        }
        
        boolean [] visit = new boolean[n+1];
        return bfs(graph,n,visit);
    }
    public static int bfs(ArrayList<ArrayList<Integer>> graph, int n,boolean[] visit) {
        Queue<int[]> queue = new LinkedList<>();
        int answer = 0;
        
        queue.add(new int[]{1,0});
        visit[1] = true;
        int maxDepth = 0;
        
        while(!queue.isEmpty()) {
            int [] cur = queue.poll();
            int v= cur[0];
            int depth = cur[1];
            
            if(maxDepth==depth) answer++;
            else if(maxDepth < depth) {
                maxDepth = depth;
                answer=1;
            }
            
            for(int i=0; i<graph.get(v).size(); i++) {
                int w = graph.get(v).get(i);
                if(!visit[w]) {
                    queue.add(new int[]{w,depth+1});
                    visit[w] = true;
                }
            }
        }
        return answer;
    }
}