import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static class people implements Comparable<people>{
        String name;
        int kor;
        int eng;
        int math;

        public people(String name, int kor, int eng, int math) {
            this.name = name;
            this.kor = kor;
            this.eng = eng;
            this.math = math;
        }

        @Override
        public int compareTo(people other) {
            if (this.kor == other.kor) {
                if (this.eng == other.eng) {
                    if (this.math == other.math) {
                        return this.name.compareTo(other.name);
                    }
                    return other.math - this.math; //내림차순
                }
                return this.eng - other.eng; //오름차순
            }
            return other.kor - this.kor;
        }

        @Override
        public String toString() {
            return name;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        List<people> arr = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            arr.add(new people(input[0], Integer.parseInt(input[1]), Integer.parseInt(input[2]), Integer.parseInt(input[3])));
        }

        Collections.sort(arr);

        for (people d : arr) {
            sb.append(d.toString()).append("\n");
        }

        System.out.println(sb);
    }
}
