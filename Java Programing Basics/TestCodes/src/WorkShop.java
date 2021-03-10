import java.util.Scanner;

public class WorkShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double TableCount = Double.parseDouble(scanner.nextLine());
        double TableLenght = Double.parseDouble(scanner.nextLine());
        double TableWeidht = Double.parseDouble(scanner.nextLine());

        double area = TableCount *(TableLenght + 0.6) * (TableWeidht + 0.6);

        double careArea = TableCount * Math.pow(TableLenght / 2, 2);
        double priceusd = area * 7 + careArea * 9;
        double leva = priceusd * 1.85;

        System.out.printf("%.2f USD\n%.2f BGN ", priceusd, leva );
    }
}
