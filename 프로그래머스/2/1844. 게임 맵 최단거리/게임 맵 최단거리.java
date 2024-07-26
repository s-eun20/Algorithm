import java.util.*;

class Solution {
    int[] dr = {0, 0, 1, -1};
    int[] dc = {1, -1, 0, 0};
    
    public int solution(int[][] maps) {
        int rowLength = maps.length;
        int colLength = maps[0].length;
        boolean[][] visited = new boolean[rowLength][colLength];
        
        int result = bfs(maps, visited);
        return result;
    }
    
    public int bfs(int[][] maps, boolean[][] visited) {
        int rowLength = maps.length;
        int colLength = maps[0].length;
        
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0, 1}); // {row, col, distance}
        visited[0][0] = true;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            int dist = cur[2];
            
            if (r == rowLength - 1 && c == colLength - 1) {
                return dist; // Reached the destination
            }
            
            for (int i = 0; i < 4; i++) {
                int nextRow = r + dr[i];
                int nextCol = c + dc[i];
                
                if (nextRow >= 0 && nextRow < rowLength && nextCol >= 0 && nextCol < colLength) {
                    if (maps[nextRow][nextCol] == 1 && !visited[nextRow][nextCol]) {
                        queue.offer(new int[]{nextRow, nextCol, dist + 1});
                        visited[nextRow][nextCol] = true;
                    }
                }
            }
        }
        
        return -1; // No path found
    }
}
