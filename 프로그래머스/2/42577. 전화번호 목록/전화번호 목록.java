import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        // phone_book 배열을 정렬합니다.
        Arrays.sort(phone_book);

        // 정렬된 배열에서 인접한 전화번호들을 비교합니다.
        for (int i = 0; i < phone_book.length - 1; i++) {
            String current = phone_book[i];
            String next = phone_book[i + 1];
            
            // current 길이만큼의 next 부분 문자열이 current와 같은지 확인합니다.
            if (next.length() >= current.length() && next.substring(0, current.length()).equals(current)) {
                return false;
            }
        }
        
        // 어떤 전화번호도 다른 전화번호의 접두사가 아닌 경우 true를 반환합니다.
        return true;
    }
}
