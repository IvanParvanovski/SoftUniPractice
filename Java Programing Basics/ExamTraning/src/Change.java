import java.util.Scanner;

public class Change {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int K = Integer.parseInt(scanner.nextLine());
        int L = Integer.parseInt(scanner.nextLine());
        int M = Integer.parseInt(scanner.nextLine());
        int N = Integer.parseInt(scanner.nextLine());

        int counter = 1;

        for (; K <= 8 ;K++){
            for (; L >= 1; L--){
               for (; M <= 8 ; M++){
                   for (;N >= 1 ; N--){
                       if (K % 2 == 0 || M % 2 == 0 && (L % 2 != 0 || N % 2 != 0 )){
                           System.out.printf("%d%d - %d%d", K , L , M, N);
                       }
                   }
               }
            }
        }
    }
}
