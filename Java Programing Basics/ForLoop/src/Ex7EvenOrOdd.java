import java.util.Scanner;

public class Ex7EvenOrOdd {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        {

            int n = Integer.parseInt(scanner.nextLine());

            int oddSum = 0;
            int evenSum = 0;

            for (int i = 1; i <= n; i++) {
                int element = Integer.parseInt(scanner.nextLine());

                if (i % 2 == 0) {
                    evenSum += element;
                } else oddSum += element;
            }

            int diff = Math.abs(oddSum - evenSum);

            if (diff == 0) {
                System.out.printf("Yes Sum = %d", oddSum);
            } else {
                System.out.printf("No Diff = %d", diff);
            }


        }
    }
}