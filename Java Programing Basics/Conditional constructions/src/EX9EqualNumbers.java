import java.util.Scanner;

public class EX9EqualNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double number1 = Double.parseDouble(scanner.nextLine());
        double number2 = Double.parseDouble(scanner.nextLine());
        double number3 = Double.parseDouble(scanner.nextLine());

        if (number1 == number2 && number2 == number3) {
            System.out.println("yes");
        }else {
            System.out.println("no");
        }

    }
}
