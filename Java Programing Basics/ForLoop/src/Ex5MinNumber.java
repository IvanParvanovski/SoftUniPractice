import java.util.Scanner;

public class Ex5MinNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < n ; i++){
            int currentN = Integer.parseInt(scanner.nextLine());

            if (currentN < min){
                min = currentN;
            }
        }
        System.out.println(min);
    }
}
