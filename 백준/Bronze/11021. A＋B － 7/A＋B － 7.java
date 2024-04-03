import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String [] input = br.readLine().split(" ");
            sb.append(String.format("Case #%d: %d\n", i + 1, Integer.parseInt(input[0]) + Integer.parseInt(input[1])));
        }

        System.out.print(sb);
    }
}
