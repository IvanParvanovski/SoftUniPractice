import java.util.Scanner;

public class Matrix2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());
        int current = 1;

        for (int rows = 0; rows < n; rows++){
            for (int cols = 0; cols < n; cols++){
                current = rows + cols + 1;
                if (current > n){
                    current = 2 * n - current;
                }
                System.out.print(current + " ");
            }
            System.out.println();
        }

    }
}
