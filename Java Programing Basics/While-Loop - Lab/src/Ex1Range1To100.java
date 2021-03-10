import java.util.Scanner;

public class Ex1Range1To100 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Еnter a number in the range [1...100]: ");
        int number = Integer.parseInt(scanner.nextLine());


        while (1 > number || number > 100.0){
            System.out.println("Invalid number!");
            System.out.print("Еnter a number in the range [1...100]: ");
            number = Integer.parseInt(scanner.nextLine());
        }
        System.out.println("The number is: " + number);
    }
}
