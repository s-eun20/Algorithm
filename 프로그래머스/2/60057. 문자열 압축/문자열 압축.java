import java.util.Stack;

public class Solution {
    public static int solution(String s) {
        int answer = s.length();

        for (int i = 0; i < s.length() / 2; i++) {
            Stack<String> stack = new Stack<>();
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < s.length() - i; j += 1 + i) {
              
                String temp = s.substring(j, j + 1 + i);

              
                if (!stack.isEmpty() && !stack.peek().equals(temp)) {
                    
                    if (stack.size() != 1) {
                        sb.append(stack.size());
                    }
                    sb.append(stack.peek());
                    
                    stack.clear();
                }

                
                stack.push(temp);
            }

            
            if (!stack.isEmpty()) {
                
                if (stack.size() != 1) {
                    sb.append(stack.size());
                }
                sb.append(stack.peek());
            }

 .
            if (s.length() % (1 + i) != 0) {
                sb.append(s.substring(s.length() - s.length() % (1 + i)));
            }

 
            answer = Math.min(answer, sb.length());

        }
        return answer;
    }
}