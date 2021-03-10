import java.util.Scanner;

public class TheThreeBrothers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double BrotherA = Double.parseDouble(scanner.nextLine());
        double BrotherB = Double.parseDouble(scanner.nextLine());
        double BrotherC = Double.parseDouble(scanner.nextLine());
        double Father = Double.parseDouble(scanner.nextLine());

        double cleaning = 1 / (1 / BrotherA + 1 / BrotherB + 1 / BrotherC);
        double cleaningWithRost = cleaning + cleaning * 15/ 100.0;
        System.out.printf("Cleaning time: %.2f\n", cleaningWithRost);

        if (Father < cleaningWithRost){
            System.out.printf("No, there isn't a surprise - shortage of time -> %.0f hours.",
            Math.ceil(cleaningWithRost - Father));
        }else {
            System.out.printf("Yes, there is a surprise - time left -> %.0f hours."
                    , Math.floor(Father - cleaningWithRost));



        }
    }
}
