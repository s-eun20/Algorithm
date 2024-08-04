public class Solution {
 
    public int solution(int[] numbers, int target) {
       return bfs(numbers,0,target,0);
    }
    
    int bfs(int[] numbers, int index, int target, int cur) {
        if(index == numbers.length){
            if(cur == target) {
                return 1;
            }
            return 0;
        }
        
        int sum = 0;
        sum += bfs(numbers,index+1,target,cur+numbers[index]);
        sum += bfs(numbers,index+1,target,cur-numbers[index]);
        
        return sum;
    }
    
}