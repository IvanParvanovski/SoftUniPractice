import java.util.Scanner;

public class FisherMan {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int budget = Integer.parseInt(scanner.nextLine());
        String season = scanner.nextLine();
        int fishermans = Integer.parseInt(scanner.nextLine());

        int PriceSpring = 3000;
        int PriceSummerAutumn = 4200;
        int PriceWinter = 2600;

        double priceForSeason = 0;

        switch (season.toLowerCase()){
            case "spring":
                priceForSeason = PriceSpring;
                break;
            case "summer":
            case "autumn":
                priceForSeason = PriceSummerAutumn;
                break;
            case "winter":
                priceForSeason = PriceWinter;
                break;
        }
        int discount = 0;
        if(fishermans <= 6 ){
                discount = 10;
        }else if (fishermans <= 11){
            discount = 15;
        }else {
            discount = 25;
        }

        double priceWithDiscount = priceForSeason - priceForSeason * discount  / 100.0;


        int additionalDiscount = 0;
        if(fishermans % 2 == 0 && !"autumn".equalsIgnoreCase(season)){
            additionalDiscount = 5;
        }
        priceWithDiscount = priceWithDiscount - priceWithDiscount * additionalDiscount / 100.0;

        double diff = budget - priceWithDiscount;
        if (budget >= priceWithDiscount){
            System.out.printf("Yes! You have %.2f leva left.", diff);

        }else {
            System.out.printf("Not enough money! You need %.2f leva.", Math.abs(diff));
        }





    }
}

