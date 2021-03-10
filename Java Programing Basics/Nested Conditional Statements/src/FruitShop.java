import java.util.Scanner;

public class FruitShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String meal = scanner.nextLine();
        String Day = scanner.nextLine();
        double count = Double.parseDouble(scanner.nextLine());
        double totalPrice = -1;

        if (Day.equals("Monday") || Day.equals("Tuesday") || Day.equals("Wednesday") || Day.equals("Thursday") || Day.equals("Friday")) {
            double banana = 2.50;
            double apple = 1.20;
            double orange = 0.85;
            double grapefruit = 1.45;
            double kiwi = 2.70;
            double pineapple = 5.50;
            double grapes = 3.85;

            if (meal.equals("banana")) {
                totalPrice = banana * count;
            } else if (meal.equals("apple")) {
                totalPrice = apple * count;
            } else if (meal.equals("orange")) {
                totalPrice = orange * count;
            } else if (meal.equals("grapefruit")) {
                totalPrice = grapefruit * count;
            } else if (meal.equals("kiwi")) {
                totalPrice = kiwi * count;
            } else if (meal.equals("pineapple")) {
                totalPrice = pineapple * count;
            } else if (meal.equals("grapes")) {
                totalPrice = grapes * count;
            }


        } else if (Day.equals("Saturday") || Day.equals("Sunday")) {
            double banana = 2.70;
            double apple = 1.25;
            double orange = 0.90;
            double grapefruit = 1.60;
            double kiwi = 3.00;
            double pineapple = 5.60;
            double grapes = 4.20;

            if (meal.equals("banana")) {
                totalPrice = banana * count;
            } else if (meal.equals("apple")) {
                totalPrice = apple * count;
            } else if (meal.equals("orange")) {
                totalPrice = orange * count;
            } else if (meal.equals("grapefruit")) {
                totalPrice = grapefruit * count;
            } else if (meal.equals("kiwi")) {
                totalPrice = kiwi * count;
            } else if (meal.equals("pineapple")) {
                totalPrice = pineapple * count;
            } else if (meal.equals("grapes")) {
                totalPrice = grapes * count;
            }


        }
        if (totalPrice >= 0) {
            System.out.println(totalPrice);
        } else
            System.out.println("error");
    }
}
