import java.util.Scanner;

public class Ex7NameWars {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String name = scanner.nextLine();
        int symbolSumMax = 0;
        String winner = "";
        while (!name.equalsIgnoreCase("Stop")){
            int symbolSum = 0;
            for (int i = 0; i < name.length(); i++) {
                char currentSymbol = name.charAt(i);
                if (Character.isAlphabetic(currentSymbol)) {
                    symbolSum += currentSymbol;
                }
                if (symbolSum > symbolSumMax) {
                    symbolSumMax = symbolSum;
                    winner = name;
                }

            }
            name = scanner.nextLine();
        }
        System.out.printf("Winner is %s - %d!", winner , symbolSumMax);

    }
}
