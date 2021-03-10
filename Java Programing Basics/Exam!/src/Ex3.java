import java.util.Scanner;

public class Ex3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String fruit = scanner.nextLine();
        String type = scanner.nextLine();
        int numSets = Integer.parseInt(scanner.nextLine());
        double sum = 0;

        if (type.equals("small")){
            if (fruit.equals("Watermelon")){
                sum += 56;
            }
            if (fruit.equals("Mango")){
                sum += 36.66;
            }
            if (fruit.equals("Pineapple")){
                sum += 42.10;
            }
            if (fruit.equals("Raspberry")){
                sum += 20;
            }
        }

        if (type.equals("big")){
            if (fruit.equals("Watermelon")){
                sum += 28.70;
            }

            if (fruit.equals("Mango")){
                sum += 19.60;
            }

            if (fruit.equals("Pineapple")){
                sum += 24.80;
            }

            if (fruit.equals("Raspberry")){
                sum += 15.20;
            }
        }
        if (type.equals("big")) {
            double money1 = sum * 5;
            double money = money1 * numSets;
            if (400 <= money && money <= 1000){
                double procent = 15 / 100.0 * money;
                double moneyProcent = money - procent;
                System.out.printf("%.2f lv.", moneyProcent);
            }else if (money > 1000){
                double procent = 50 / 100.0 * money;
                double moneyProcent = money - procent;
                System.out.printf("%.2f lv.", moneyProcent);
            }else
                System.out.printf("%.2f lv.", money);
        }

        if (type.equals("small")) {
            double money1 = sum * numSets ;
            double money = money1 * 2;
            if (400 <= money && money <= 1000){
                double procent = 15 / 100.0 * money;
                double moneyProcent = money - procent;
                System.out.printf("%.2f lv.", moneyProcent);
            } else if (money > 1000){
                double procent = 50 / 100.0 * money;
                double moneyProcent = money - procent;
                System.out.printf("%.2f lv.", moneyProcent);
            }else
                System.out.printf("%.2f lv.", money);
        }

    }
}
