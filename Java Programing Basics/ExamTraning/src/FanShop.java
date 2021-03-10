import java.util.Scanner;

public class FanShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int money = Integer.parseInt(scanner.nextLine());
        int countClothes = Integer.parseInt(scanner.nextLine());
        int sum = 0;

        for (int i = 1; i <= countClothes ; i++){
            String cloth = scanner.nextLine();

            if (cloth.equalsIgnoreCase("hoodie")){
                sum += 30;
            }

            if (cloth.equalsIgnoreCase("keychain")){
                sum += 4;
            }

            if (cloth.equalsIgnoreCase("T-shirt")){
                sum += 20;
            }

            if (cloth.equalsIgnoreCase("flag")){
                sum += 15;
            }

            if (cloth.equalsIgnoreCase("sticker")){
                sum += 1;
            }
        }

        int diff = money - sum;

        if (sum <= money){
            System.out.printf("You bought %d items and left with %d lv.", countClothes , diff);
        }

        if (sum > money)
            System.out.printf("Not enough money, you need %d more lv.", Math.abs(diff));
    }
}
