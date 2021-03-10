import java.util.Scanner;

public class Birthday {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a = Double.parseDouble(scanner.nextLine());
        double b = Double.parseDouble(scanner.nextLine());
        double c = Double.parseDouble(scanner.nextLine());
        double area = a * b * c;
        System.out.println(area);


        System.out.println(area * 0.001);



        double p = Double.parseDouble(scanner.nextLine());
        double ch = 0.01;
        double procent = p * ch;
        System.out.println(procent);

        System.out.println((a * b * c * 0.001) *(1-procent));
    }
}
