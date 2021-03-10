import java.util.Scanner;

public class Homework {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = Double.parseDouble(scanner.nextLine());
        double b = Double.parseDouble(scanner.nextLine());
        double c = Double.parseDouble(scanner.nextLine());
        double area = a * b * c;
        double p = Double.parseDouble(scanner.nextLine());
        double procent = p * 0.01;
        System.out.printf("%.3f",(area * 0.001) *(1-procent));
    }
}
