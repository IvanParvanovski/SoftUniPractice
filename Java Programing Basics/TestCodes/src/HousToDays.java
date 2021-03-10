import java.util.Scanner;

public class HousToDays {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double Hours = Double.parseDouble(scanner.nextLine());
        double Days = Hours / 24;
        System.out.printf("%.0f", Days);
    }
}
