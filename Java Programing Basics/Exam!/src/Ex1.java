import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int alphinisths = Integer.parseInt(scanner.nextLine());
        int karabinels = Integer.parseInt(scanner.nextLine());
        int ropes = Integer.parseInt(scanner.nextLine());
        int pickels = Integer.parseInt(scanner.nextLine());

        double moneyKarabinels = karabinels * 36;
        double moneyRopes = ropes * 3.60;
        double moneyPickels = pickels * 19.80;

        double moneyForOne = moneyKarabinels + moneyPickels + moneyRopes;
        double moneyForAll = moneyForOne * alphinisths;
        double moneyDDS = 20 / 100.0 * moneyForAll;

        double moneyNeed = moneyForAll + moneyDDS;
        System.out.printf("%.2f", moneyNeed);


    }
}
