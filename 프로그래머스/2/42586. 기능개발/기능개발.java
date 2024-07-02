import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        Stack<Integer> stack = new Stack<>();
        
        // 각 작업의 완료 날짜 계산
        for (int i = 0; i < progresses.length; i++) {
            int remainingWork = 100 - progresses[i];
            int days = (remainingWork + speeds[i] - 1) / speeds[i]; 
            stack.push(days);
        }
        
        List<Integer> answerList = new ArrayList<>();
        while (!stack.isEmpty()) {
            int currentDay = stack.remove(0);
            int count = 1;
            
            while (!stack.isEmpty() && stack.get(0) <= currentDay) {
                count++;
                stack.remove(0);
            }
            
            answerList.add(count);
        }
        
        // 결과 배열로 변환
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}
