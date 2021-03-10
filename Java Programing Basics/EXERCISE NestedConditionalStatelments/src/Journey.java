import java.util.Scanner;

public class Journey {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double money = Double.parseDouble(scanner.nextLine());
        String season = scanner.nextLine();

        if (money <= 100) {
            if (season.equalsIgnoreCase("Summer")) {
                double spendMoney = (30 / 100.0) * money;
                System.out.println("Somewhere in Bulgaria");
                System.out.printf("Camp - %.2f", spendMoney);
            }

            if (season.equalsIgnoreCase("Winter")) {
                double spendMoney = (70 / 100.0) * money;
                System.out.println("Somewhere in Bulgaria");
                System.out.printf("Hotel - %.2f", spendMoney);
            }
        }

        if (money <= 1000 && money > 100) {
            if (season.equalsIgnoreCase("Summer")) {
                double spendMoney = (40 / 100.0) * money;
                System.out.println("Somewhere in Balkans");
                System.out.printf("Camp - %.2f", spendMoney);
            }

            if (season.equalsIgnoreCase("Winter")) {
                double spendMoney = (80 / 100.0) * money;
                System.out.println("Somewhere in Balkans");
                System.out.printf("Hotel - %.2f", spendMoney);
            }
        }

            if (money > 1000) {
                if (season.equalsIgnoreCase("Summer")) {
                    double spendMoney = (90 / 100.0) * money;
                    System.out.println("Somewhere in Europe");
                    System.out.printf("Hotel - %.2f", spendMoney);
                }

                if (season.equalsIgnoreCase("Winter")) {
                    double spendMoney = (90 / 100.0) * money;
                    System.out.println("Somewhere in Europe");
                    System.out.printf("Hotel - %.2f", spendMoney);
                }


            }


    }
}