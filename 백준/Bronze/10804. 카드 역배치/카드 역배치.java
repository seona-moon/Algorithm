import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] arr = new int[21];
        for (int i = 1; i < 21; i++) {
            arr[i] = i;
        }

        // 10회의 입력
        for (int i = 0; i < 10; i++) {
            int start = in.nextInt();
            int end = in.nextInt();

            int n = (end-start) / 2;
            for (int j = 0; j <= n; j++) {
                // swap(arr[start+j], arr[end-j])
                int tmp = arr[start + j];
                arr[start + j] = arr[end - j];
                arr[end - j] = tmp;
            }
        }
        for (int i = 1; i < 21; i++) {
            System.out.print(arr[i]+" ");
        }
        in.close();
    }
}