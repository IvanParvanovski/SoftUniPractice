import java.util.Scanner;

public class SomeThings {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double x1 = Double.parseDouble(scanner.nextLine());
        double y1 = Double.parseDouble(scanner.nextLine());

        double x2 = Double.parseDouble(scanner.nextLine());
        double y2 = Double.parseDouble(scanner.nextLine());

        double length = Math.abs(x1-x2);
        double weh = Math.abs(y1-y2);
        double area = length * weh;
        System.out.println(area);


        double pere = 2 * (length + weh);
        System.out.println(pere);

}
}
