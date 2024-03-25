import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // 동전의 종류
        int k = in.nextInt(); // 동전 가치의 합
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }

        int cnt = 0;
        // 그리디 알고리즘으로 문제 풀이 (가장 큰 단위부터 계산)
        for (int i = n - 1; i >= 0; i--) {
            if (k >= arr[i]) {
                cnt += k/arr[i];
                k %= arr[i];
            }
        }
        System.out.println(cnt);

        in.close();
    }
}