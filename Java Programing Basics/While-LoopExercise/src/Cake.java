import java.util.Scanner;

public class Cake {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int piecesOfCake = Integer.parseInt(scanner.nextLine());
        int w = Integer.parseInt(scanner.nextLine());
        int l = Integer.parseInt(scanner.nextLine());

        int areaOfCake = w * l;

        int piecesPcanEat = areaOfCake / piecesOfCake;

        while (piecesOfCake >= piecesPcanEat){
            int piecesOfCakeLeft = piecesOfCake - piecesPcanEat;
            String command = scanner.nextLine();
            if (command.equalsIgnoreCase("STOP")){
                break;
            }
            System.out.printf("%d pieces are left.", piecesOfCakeLeft);
        }

        while (piecesOfCake < piecesPcanEat){
            int piecesOfCakeNeed = piecesPcanEat - piecesOfCake;
            System.out.printf("No more cake left! You need %d pieces more.", Math.abs(piecesOfCakeNeed));
        }
    }
}
