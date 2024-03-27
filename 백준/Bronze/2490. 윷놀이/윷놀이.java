import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        String[] arr = {"D", "C", "B", "A", "E"};
        Scanner in = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            int sum = 0;
            for (int j = 0; j < 4; j++) {
                sum += in.nextInt();
            }
            System.out.println(arr[sum]);
        }
        in.close();
    }
}