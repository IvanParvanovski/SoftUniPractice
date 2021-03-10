import java.util.Scanner;

public class SumSeconds {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int player1 = Integer.parseInt(scanner.nextLine());
        int player2 = Integer.parseInt(scanner.nextLine());
        int player3 = Integer.parseInt(scanner.nextLine());

        int sumSeconds = (player1 + player2 + player3);

        int minutes = sumSeconds / 60;
        int seconds = sumSeconds % 60;

        if (10 > seconds){
            System.out.printf("%d:0%d", minutes, seconds);
        }else {
            System.out.printf("%d:%d", minutes , seconds);
        }


        }
    }

