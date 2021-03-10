import java.util.Scanner;

public class BeerAndChips {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String nameFan = scanner.nextLine();
        double money = Double.parseDouble(scanner.nextLine());
        int bottlesBira = Integer.parseInt(scanner.nextLine());
        int chipsPackets = Integer.parseInt(scanner.nextLine());

        double beer = 1.20;
        double moneyBeer =  beer * bottlesBira;
        double money1PackerChips = 45 / 100.0 * moneyBeer;
        double moneyChips = money1PackerChips * chipsPackets;
        double moneyChipsBigNum = Math.ceil(moneyChips);
        double moneyNeed = moneyChipsBigNum + moneyBeer;

        double moneyDiff = money - moneyNeed;

        if (moneyNeed <= money){
            System.out.printf("%s bought a snack and has %.2f leva left.", nameFan , moneyDiff);
        }else
            System.out.printf("%s needs %.2f more leva!", nameFan , Math.abs(moneyDiff));

    }
}
