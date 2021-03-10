import java.util.Scanner;

public class SummerQutfit {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int degrees = Integer.parseInt(scanner.nextLine());
        String TypeOfDay = scanner.nextLine();

        if (TypeOfDay.equalsIgnoreCase("Morning") && 10 <= degrees && degrees <= 18){
           System.out.printf("It's %d degrees, get your Sweatshirt and Sneakers.", degrees);
        }else if (TypeOfDay.equalsIgnoreCase("Morning") && 18 <= degrees && degrees <= 24){
            System.out.printf("It's %d degrees, get your Shirt and Moccasins.", degrees);
        }else if (TypeOfDay.equalsIgnoreCase("Morning") && degrees >= 25){
            System.out.printf("It's %d degrees, get your T-Shirt and Sandals.", degrees); }


            if (TypeOfDay.equalsIgnoreCase("Afternoon") && 10 <= degrees && degrees <= 18){
            System.out.printf("It's %d degrees, get your Shirt and Moccasins.", degrees);
        }else if (TypeOfDay.equalsIgnoreCase("Afternoon") && 18 <= degrees && degrees <= 24){
            System.out.printf("It's %d degrees, get your T-Shirt and Sandals.", degrees);
        }else if (TypeOfDay.equalsIgnoreCase("Afternoon") && degrees >= 25) {
            System.out.printf("It's %d degrees, get your Swim Suit and Barefoot.", degrees); }


            if (TypeOfDay.equalsIgnoreCase("Evening") && 10 <= degrees && degrees <= 18){
            System.out.printf("It's %d degrees, get your Shirt and Moccasins.", degrees);
        }else if (TypeOfDay.equalsIgnoreCase("Evening") && 18 <= degrees && degrees <= 24){
            System.out.printf("It's %d degrees, get your Shirt and Moccasins.", degrees);
        }else if (TypeOfDay.equalsIgnoreCase("Evening") && degrees >= 25){
            System.out.printf("It's %d degrees, get your Shirt and Moccasins.", degrees); }

    }
}
