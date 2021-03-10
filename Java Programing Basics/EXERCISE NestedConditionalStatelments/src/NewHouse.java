import java.util.Scanner;

public class NewHouse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String flower = scanner.nextLine();
        int count = Integer.parseInt(scanner.nextLine());
        int money = Integer.parseInt(scanner.nextLine());
        double rose = 5;
        double dahlia = 3.80;
        double tulips = 2.80;
        double narcissus = 3;
        double gladious = 2.50;

        if (flower.equalsIgnoreCase("rose")) {
            double moneyForRoses = rose * count;

            double LeftMoneyRoses = money - moneyForRoses;
            double MoneyWithProcentForRoses = moneyForRoses - (10 / 100.0 * moneyForRoses);
            double MoneyLeftWithProcentRoses = money - MoneyWithProcentForRoses;
            double MoneyYouNeedMoreForRoses = moneyForRoses - money;

            if (flower.equalsIgnoreCase("roses") && moneyForRoses <= money && count >= 80) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, MoneyLeftWithProcentRoses);
            } else if (flower.equalsIgnoreCase("roses") && moneyForRoses <= money) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, LeftMoneyRoses);
            } else if (money > moneyForRoses){
                System.out.printf("Not enough money, you need %.2f leva more.", MoneyYouNeedMoreForRoses); }
        }

        if (flower.equalsIgnoreCase("dahlia")) {

            double moneyForDahlias = dahlia * count;

            double LeftMoneyDahlias = money - moneyForDahlias;
            double MoneyWithProcentForDahlias = moneyForDahlias - (15 / 100.0 * moneyForDahlias);
            double MoneyLeftWithProcentDahlias = money - MoneyWithProcentForDahlias;
            double MoneyYouNeedMoreForDhalias = MoneyWithProcentForDahlias - money;

            if (flower.equalsIgnoreCase("Dahlias") && moneyForDahlias <= money && count >= 90) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, MoneyLeftWithProcentDahlias);
            } else if (flower.equalsIgnoreCase("Dahlias") && moneyForDahlias <= money) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, LeftMoneyDahlias);
            }else
                System.out.printf("Not enough money, you need %.2f leva more.", MoneyYouNeedMoreForDhalias );

        }

        if (flower.equalsIgnoreCase("tulips")) {
            double moneyForTulips = tulips * count;

            double LeftMoneyTulips = money - moneyForTulips;
            double MoneyWithProcentForTulips = moneyForTulips - (15 / 100.0 * moneyForTulips);
            double MoneyLeftWithProcentTulips = money - MoneyWithProcentForTulips;
            double MoneyYouNeedMoreForTulips = MoneyWithProcentForTulips - money;


            if (flower.equalsIgnoreCase("tulips") && moneyForTulips <= money && count >= 80) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, MoneyLeftWithProcentTulips);
            } else if (flower.equalsIgnoreCase("Tulips") && moneyForTulips <= money) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, LeftMoneyTulips);
            }else
                System.out.printf("Not enough money, you need %.2f leva more.", MoneyYouNeedMoreForTulips );
        }

        if (flower.equalsIgnoreCase("narcissus")) {
            double moneyForNarcissus = narcissus * count;

            double LeftMoneyNarcissus = money - moneyForNarcissus;
            double MoneyWithProcentForNarcissus = moneyForNarcissus - (15 / 100.0 * moneyForNarcissus);
            double MoneyLeftWithProcentNarcissus = money - MoneyWithProcentForNarcissus;
            double MoneyYouNeedMoreForNarcissus = MoneyWithProcentForNarcissus - money;

            if (flower.equalsIgnoreCase("Narcissus") && moneyForNarcissus <= money && count >= 120) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, MoneyLeftWithProcentNarcissus);
            } else if (flower.equalsIgnoreCase("Narcissus") && moneyForNarcissus <= money) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, LeftMoneyNarcissus);
            }else
                System.out.printf("Not enough money, you need %.2f leva more.", MoneyYouNeedMoreForNarcissus);
        }

        if (flower.equalsIgnoreCase("gladiolus")) {
            double moneyForGladiolus = gladious * count;

            double LeftMoneyGladiolus = money - moneyForGladiolus;
            double MoneyWithProcentForGladiolus = moneyForGladiolus - (20 / 100.0 * moneyForGladiolus);
            double MoneyLeftWithProcentGladiolus = money - MoneyWithProcentForGladiolus;
            double MoneyYouNeedMoreForGladiolus = MoneyWithProcentForGladiolus - money;

            if (flower.equalsIgnoreCase("Gladiolus") && moneyForGladiolus <= money && count >= 80) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, MoneyLeftWithProcentGladiolus);
            } else if (flower.equalsIgnoreCase("Gladiolus") && moneyForGladiolus <= money) {
                System.out.printf("Hey, you have a great garden with %d %s and %.2f leva left", count, flower, LeftMoneyGladiolus);
            }else
                System.out.printf("Not enough money, you need %.2f leva more.", MoneyYouNeedMoreForGladiolus);

        }
    }
}

