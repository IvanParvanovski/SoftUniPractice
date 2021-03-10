import java.util.Scanner;

public class TheBestPlayer {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
            String playerName = scanner.nextLine();
            int goals = Integer.parseInt(scanner.nextLine());
            int goalMax = Integer.MIN_VALUE;
            String bestPlayer = "";

            for ( ; goalMax <= 10  ; ){
                if (goalMax < goals){
                    goalMax = goals;
                    bestPlayer = playerName;
                    }
                if (goalMax >= 10){
                    break;
                }
                playerName = scanner.nextLine();
                if (playerName.equalsIgnoreCase("END")){
                    break;
                }
                goals = Integer.parseInt(scanner.nextLine());

            }
            if (goalMax >= 3) {
                System.out.printf("%s is the best player!%n", bestPlayer);
                System.out.printf("He has scored %d goals and made a hat-trick !!!", goalMax );
            }

            if (goalMax < 3) {
            System.out.printf("%s is the best player!%n", bestPlayer);
            System.out.printf("He has scored %d goals." , goalMax );
            }

    }
}
