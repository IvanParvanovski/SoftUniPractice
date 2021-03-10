import java.util.Scanner;

public class Exercise {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String building = scanner.nextLine();
        int redove = Integer.parseInt(scanner.nextLine());
        int coloni = Integer.parseInt(scanner.nextLine());

        double lice = redove * coloni;

        if (building.equalsIgnoreCase("Premiere")){
            double money = lice * 12.00;
            System.out.printf("%.2f leva", money);
        }else if (building.equalsIgnoreCase("Normal")){
            double money = lice * 7.50;
            System.out.printf("%.2f leva", money);
        }else if (building.equalsIgnoreCase("Discount")){
            double money = lice * 5.00;
            System.out.printf("%.2f leva", money );
        }

    }
}
