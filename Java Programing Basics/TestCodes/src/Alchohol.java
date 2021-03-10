import java.util.Scanner;

public class Alchohol {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double priceWhiskey = Double.parseDouble(scanner.nextLine());
        double beer = Double.parseDouble(scanner.nextLine());
        double wine = Double.parseDouble(scanner.nextLine());
        double rakia = Double.parseDouble(scanner.nextLine());
        double whiskey = Double.parseDouble(scanner.nextLine());

        double priceRakija = priceWhiskey / 2;
        double priceWine = priceRakija * (1 - 40.0 / 100);
        double priceBeer = priceRakija - priceRakija * 80 / 100;

        double priceAllWhiskey = priceWhiskey * whiskey;
        double priceAllBeer = priceBeer * beer;
        double priceAllWine = priceWine * wine;
        double priceAllRakija = priceRakija * rakia;
        double allPrice = priceAllWhiskey + priceAllBeer + priceAllWine + priceAllRakija;
        System.out.printf("%.2f", allPrice);
    }
}
