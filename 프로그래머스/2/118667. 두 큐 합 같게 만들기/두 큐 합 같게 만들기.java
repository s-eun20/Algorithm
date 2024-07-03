import java.util.*;

class Solution {
    public int solution(int[] queue1Arr, int[] queue2Arr) {
        Queue<Integer> queue1 = new LinkedList<>();
        Queue<Integer> queue2 = new LinkedList<>();

        for (int num : queue1Arr) {
            queue1.offer(num);
        }
        for (int num : queue2Arr) {
            queue2.offer(num);
        }

        return equalizeQueueSums(queue1, queue2);
    }
    
    public static int equalizeQueueSums(Queue<Integer> queue1, Queue<Integer> queue2) {
        long sum1 = queue1.stream().mapToInt(Integer::intValue).sum();
        long sum2 = queue2.stream().mapToInt(Integer::intValue).sum();

        long totalSum = sum1 + sum2;

        // If the total sum is odd, it's impossible to split equally
        if (totalSum % 2 != 0) {
            return -1;
        }

        long target = totalSum / 2;
        int operations = 0;
        int maxOperations = queue1.size() * 2 + queue2.size() * 2;

        while (sum1 != target && operations <= maxOperations) {
            if (sum1 > target) {
                int value = queue1.poll();
                sum1 -= value;
                queue2.offer(value);
                sum2 += value;
            } else {
                int value = queue2.poll();
                sum2 -= value;
                queue1.offer(value);
                sum1 += value;
            }
            operations++;
        }

        return sum1 == target ? operations : -1;
    }
}
