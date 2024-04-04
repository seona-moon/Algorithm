import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        char[] input = br.readLine().toCharArray();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += input[i]-'0';
        }
        System.out.print(sum);
    }
}
