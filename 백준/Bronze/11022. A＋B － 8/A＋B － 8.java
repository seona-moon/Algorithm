import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        for (int i = 1; i <= t; i++) {
            String [] input = br.readLine().split(" ");
            sb.append("Case #"+i+": "+input[0]+" + "+input[1]+" = ");
            sb.append(Integer.parseInt(input[0])+Integer.parseInt(input[1])+"\n");
        }

        System.out.print(sb);
    }
}
