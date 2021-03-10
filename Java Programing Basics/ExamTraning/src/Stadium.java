import java.util.Scanner;

public class Stadium {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int sectors = Integer.parseInt(scanner.nextLine());
        int capacityOfStadium = Integer.parseInt(scanner.nextLine());
        double moneyTicket = Double.parseDouble(scanner.nextLine());


        double moneyAll = capacityOfStadium * moneyTicket;
        double moneySectors = moneyAll / sectors;

        double moneyCharity =  (moneyAll - (moneySectors * 0.75)) / 8;
        System.out.printf("Total income - %.2f BGN%n", moneyAll);
        System.out.printf("Money for charity - %.2f BGN", moneyCharity);




    }
}
