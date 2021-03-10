import java.util.Scanner;

public class Cake {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int l = Integer.parseInt(scanner.nextLine());
        int w = Integer.parseInt(scanner.nextLine());
        int area = l * w;
        int pieces = 0;
        int piecesNow = 0;
        int piecesBefore = 0;

        while (area >= pieces){
            pieces = Integer.parseInt(scanner.nextLine());
            piecesBefore = pieces;
            piecesNow = pieces + piecesBefore;
        }
    }
}
