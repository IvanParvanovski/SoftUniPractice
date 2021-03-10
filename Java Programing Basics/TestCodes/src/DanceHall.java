import java.util.Scanner;

public class DanceHall {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double L = Double.parseDouble(scanner.nextLine());
        double W = Double.parseDouble(scanner.nextLine());
        double area = L * W;

        double BenchArea = area / 10;

        double A = Double.parseDouble(scanner.nextLine());
        double shelf = A * A;

        double people = ((area - (BenchArea + shelf)) / 0.704);

        double people1 = Math.floor(people);

        System.out.printf("%.0f", people1);

    }
}
