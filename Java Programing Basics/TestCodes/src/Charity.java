import java.util.Scanner;

public class Charity {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double days = Double.parseDouble(scanner.nextLine());
        double backers = Double.parseDouble(scanner.nextLine());
        double cake = Double.parseDouble(scanner.nextLine());
        double gofreta = Double.parseDouble(scanner.nextLine());
        double pancacke = Double.parseDouble(scanner.nextLine());
        double sweet = (cake * 45) + (gofreta * 5.80) + (pancacke * 3.20);
        double PriceForMaterials = sweet * backers;
        double MoneyForDays = PriceForMaterials * days;
        double MoneyForCharity = MoneyForDays - (0.125 * MoneyForDays);
        System.out.printf("%.2f", MoneyForCharity);
    }
}
