import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        char[] arr = in.nextLine().toCharArray();

        Arrays.sort(arr);

        for (int i = arr.length-1; i >= 0 ; i--) {
            // 뒤에서부터 출력
            System.out.print(arr[i]);
        }

        in.close();
    }
}