import java.util.Scanner;

public class Ex10TicketsForMatch {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double money = Integer.parseInt(scanner.nextLine());
        String type = scanner.nextLine();
        int countChildren = Integer.parseInt(scanner.nextLine());

        double VIP = 499.99;
        double Normal = 249.99;
        double moneyForTrans = 0;
        double moneyleft = 0;

        if (countChildren <= 4) {
            moneyForTrans = 75 / 100.0 * money;
            moneyleft = money - moneyForTrans;
        }

        if (countChildren <= 9 && countChildren > 4) {
            moneyForTrans = 60 / 100.0 * money;
            moneyleft = money - moneyForTrans;
        }

        if (countChildren <= 24 && countChildren > 9) {
            moneyForTrans = 50 / 100.0 * money;
            moneyleft = money - moneyForTrans;
        }

        if (countChildren <= 49 && countChildren > 24) {
            moneyForTrans = 40 / 100.0 * money;
            moneyleft = money - moneyForTrans;
        }

        if (countChildren > 50 ) {
            moneyForTrans = 25 / 100.0 * money;
            moneyleft = money - moneyForTrans;
        }


        double VipTicketNM = VIP * countChildren;
        double NormalTicketNM = Normal * countChildren;

        if (type.equals("VIP") && moneyleft < VipTicketNM) {
            double diff = VipTicketNM - moneyleft;
            System.out.printf("Not enough money! You need %.2f leva.", diff);
        }

        if (type.equals("VIP") && moneyleft >= VipTicketNM) {
            double moneyLeftVip = moneyleft - VipTicketNM;
            System.out.printf("Yes! You have %.2f leva left.", moneyLeftVip);
        }

        if (type.equals("Normal") && moneyleft < NormalTicketNM) {
            double diff = NormalTicketNM - moneyleft;
            System.out.printf("Not enough money! You need %.2f leva.", diff);
        }

        if (type.equals("Normal") && moneyleft >= NormalTicketNM) {
            double moneyLeftNormal = moneyleft - NormalTicketNM;
            System.out.printf("Yes! You have %.2f leva left.", moneyLeftNormal);
        }



    }
}
