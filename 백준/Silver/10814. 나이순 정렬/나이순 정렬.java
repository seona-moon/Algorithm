import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static class people implements Comparable<people>{
        int idx;
        int age;
        String name;

        public people(int idx, int age, String name) {
            this.idx = idx;
            this.age = age;
            this.name = name;
        }

        @Override
        public int compareTo(people other) {
            if (this.age == other.age) {
                return this.idx - other.idx;
            }
            return this.age - other.age;
        }

        @Override
        public String toString() {
            return age + " " + name;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        List<people> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            arr.add(new people(i, Integer.parseInt(input[0]), input[1]));
        }

        Collections.sort(arr);

        for (people d : arr) {
            sb.append(d.toString()).append("\n");
        }

        System.out.println(sb);
    }
}
