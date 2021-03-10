import java.awt.desktop.SystemSleepEvent;
import java.util.Scanner;

public class SeaTrip {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double moneyFood = Integer.parseInt(scanner.nextLine());
        double moneySuveniri= Integer.parseInt(scanner.nextLine());
        double moneyHotel = Integer.parseInt(scanner.nextLine());

        double priceNeedFor100Km = 420 / 100.0 * 7;
        double priceToSea = priceNeedFor100Km * 1.85;
        double priceSandF = (moneySuveniri + moneyFood) * 3;

              double moneyFirstDayHotel = (10 / 100.0) * moneyHotel;
              double moneyLeftFirstDay = moneyHotel - moneyFirstDayHotel;

              double moneySecondDayHotel = 15 / 100.0 * moneyHotel;
              double moneyLeftSecondDay = moneyHotel - moneySecondDayHotel;

              double moneyThirdDayHotel = 20 / 100.0 * moneyHotel;
              double moneyLeftThird = moneyHotel - moneyThirdDayHotel;

              double moneyHotelSum = moneyLeftThird + moneyLeftFirstDay + moneyLeftSecondDay;

              double moneyNeed = priceSandF + priceToSea + moneyHotelSum;
              System.out.printf("Money needed: %.2f", moneyNeed);

    }
}
