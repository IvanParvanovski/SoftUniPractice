import java.util.Scanner;


public class Salary {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());
        int money = Integer.parseInt(scanner.nextLine());
        int money2 = money;

        for (int i = 1; i <= n; i++) {
            String web = scanner.nextLine();

            if (web.equalsIgnoreCase("Facebook")) {
                money -= 150;
            }

            if (web.equalsIgnoreCase("Instagram")) {
                money -= 100;
            }

            if (web.equalsIgnoreCase("Reddit")) {
                money -= 50;
            } else
                money -= 0;
        }


        if (money <= 0) {
            System.out.println("You have lost your salary.");
        }else
            System.out.println(money);
    }
}
