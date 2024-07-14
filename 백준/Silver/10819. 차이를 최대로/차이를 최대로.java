import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] array = new int[n];

        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        // 모든 순열을 저장할 리스트
        List<int[]> permutations = new ArrayList<>();
        boolean[] used = new boolean[n];

        // 순열 생성
        generatePermutations(array, new int[n], used, 0, permutations);

        int maxDifference = 0;

        // 각 순열에 대해 차이 계산
        for (int[] perm : permutations) {
            int currentDifference = calculateDifference(perm);
            maxDifference = Math.max(maxDifference, currentDifference);
        }

        System.out.println(maxDifference);
    }

    private static void generatePermutations(int[] array, int[] current, boolean[] used, int depth, List<int[]> permutations) {
        if (depth == array.length) {
            permutations.add(current.clone());
            return;
        }

        for (int i = 0; i < array.length; i++) {
            if (!used[i]) {
                used[i] = true;
                current[depth] = array[i];
                generatePermutations(array, current, used, depth + 1, permutations);
                used[i] = false;
            }
        }
    }

    private static int calculateDifference(int[] perm) {
        int sum = 0;
        for (int i = 0; i < perm.length - 1; i++) {
            sum += Math.abs(perm[i] - perm[i + 1]);
        }
        return sum;
    }
}
