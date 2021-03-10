import java.util.Scanner;

public class Ex2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double secondsRecord = Double.parseDouble(scanner.nextLine());
        double meters = Double.parseDouble(scanner.nextLine());
        double timeSeconds = Double.parseDouble(scanner.nextLine());

        double mustClimbSeconds = meters * timeSeconds;

        double timeWithRocks = (meters / 50);

        double timeAbs = Math.floor(timeWithRocks);
        double timeN13 = timeAbs * 30;

        double AllTime = mustClimbSeconds + timeN13;
        double diff = AllTime - secondsRecord;

        if (secondsRecord <= AllTime){
            System.out.printf("No! He was %.2f seconds slower.", diff);
        }else {
            System.out.printf("Yes! The new record is %.2f seconds.", AllTime);
        }
    }
}
