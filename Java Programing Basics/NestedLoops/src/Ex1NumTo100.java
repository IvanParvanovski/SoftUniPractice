import java.util.Scanner;

public class Ex1NumTo100 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());

        for (int i = n; i > 0 ; i-- ){
            System.out.println(i);
        }

    }
}
