import java.util.Scanner;

public class Moneti {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double money = Double.parseDouble(scanner.nextLine());
        double moneyAtCoins = money * 100;
        double coins = 0;

        while (moneyAtCoins >= 200){
            coins += 1;
            moneyAtCoins -= 200;
        }

        while (moneyAtCoins >= 100 && moneyAtCoins < 200){
            coins += 1;
            moneyAtCoins -= 100;
        }

        while (moneyAtCoins >= 50 && moneyAtCoins < 100){
            coins += 1;
            moneyAtCoins -= 50;
        }

        while (moneyAtCoins >= 20 && moneyAtCoins < 50){
            coins += 1;
            moneyAtCoins -= 20;
        }

        while (moneyAtCoins >= 10 && moneyAtCoins < 20){
            coins += 1;
            moneyAtCoins -=  10;
        }

        while (moneyAtCoins >= 5 && moneyAtCoins < 10){
            coins += 1;
            moneyAtCoins -= 5;
        }

        while (moneyAtCoins >= 2 && moneyAtCoins < 5){
            coins += 1;
            moneyAtCoins -= 2;
        }

        while ( moneyAtCoins >= 1 && moneyAtCoins < 2){
            coins +=1;
            moneyAtCoins -= 1;
        }

        System.out.printf("%.0f", coins);
    }
}
