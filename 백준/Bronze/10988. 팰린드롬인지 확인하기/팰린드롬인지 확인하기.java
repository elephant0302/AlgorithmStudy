import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int ans = 1; // 기본적으로 회문이라고 가정하고 시작합니다.
        int cnt = s.length();
        for (int i = 0; i < cnt / 2; i++) {
            if (s.charAt(i) != s.charAt(cnt - i - 1)) {
                ans = 0; // 한 번이라도 문자가 맞지 않으면 회문이 아니므로 0을 할당합니다.
                break;
            }
        }
        System.out.println(ans); // 1이면 회문, 0이면 회문이 아님을 출력합니다.
    }
}
