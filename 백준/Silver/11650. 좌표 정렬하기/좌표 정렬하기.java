import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static class dot implements Comparable<dot>{
        int x;
        int y;

        public dot(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(dot other) {
            if (this.x == other.x) {
                return this.y - other.y;
            }
            return this.x - other.x;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        List<dot> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            arr.add(new dot(Integer.parseInt(input[0]), Integer.parseInt(input[1])));
        }

        //좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
        Collections.sort(arr);

        for (dot d : arr) {
            sb.append(d.x).append(" ").append(d.y).append("\n");
        }

        System.out.println(sb);
    }
}
