import java.util.Scanner;

public class NumberSEx4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String command;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        while (true) {
            command = scanner.nextLine();


            if (command.equalsIgnoreCase("END")) {
                break;
            }
            int currentNumber = Integer.parseInt(command);

            if (currentNumber < min) {
                min = currentNumber;
            }


            if (currentNumber > max) {
                max = currentNumber;
            }
        }
        System.out.printf("Max number: %d\n", max);
        System.out.printf("Min number: %d", min);
    }
}