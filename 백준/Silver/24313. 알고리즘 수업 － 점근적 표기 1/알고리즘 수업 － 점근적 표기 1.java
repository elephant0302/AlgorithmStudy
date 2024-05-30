import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a1 = sc.nextInt(); // f(n)의 n의 계수
        int a0 = sc.nextInt(); // f(n)의 상수항
        int c = sc.nextInt();  // Big O 표기법의 상수 c
        int n0 = sc.nextInt(); // Big O 표기법의 시작하는 n의 값

        boolean isBigO = true;
        for (int n = n0; n <= 100; n++) { // n0부터 100까지 확인 (n0 이상 모든 n을 검사하는 것은 불가능하므로 적당한 범위 설정)
            int fn = a1 * n + a0;
            int cn = c * n;
            if (fn > cn) {
                isBigO = false;
                break;
            }
        }

        System.out.println(isBigO ? 1 : 0);
    }
}