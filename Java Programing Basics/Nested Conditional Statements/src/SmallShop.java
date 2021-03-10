import java.util.Scanner;

public class SmallShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String product = scanner.nextLine();
        String city = scanner.nextLine();
        double count = Double.parseDouble(scanner.nextLine());




        if (city.equals("Sofia")) {
            double coffee = 0.50;
            double water = 0.80;
            double beer = 1.20;
            double sweets = 1.45;
            double peanuts =1.60;

            if (product.equals("coffee")){
                java.lang.System.out.println(  coffee * count);
            }else if (product.equals("water")){
                java.lang.System.out.println(  water * count);
            }else if (product.equals("beer")){
                java.lang.System.out.println(  beer * count);
            }else if (product.equals("sweets")){
                java.lang.System.out.println(  sweets * count);
            }else if (product.equals("peanuts")){
                java.lang.System.out.println(peanuts * count);
            }


        }
        if (city.equals("Plovdiv")){
            double coffee = 0.40;
            double water = 0.70;
            double beer = 1.15;
            double sweets = 1.30;
            double peanuts =1.50;

            if (product.equals("coffee")){
                java.lang.System.out.println(coffee * count);
            }else if (product.equals("water")){
                java.lang.System.out.println(water * count);
            }else if (product.equals("beer")){
                java.lang.System.out.println(beer * count);
            }else if (product.equals("sweets")){
                java.lang.System.out.println(sweets * count);
            }else if (product.equals("peanuts")){
                java.lang.System.out.println(peanuts * count);
            }


        }
        if (city.equals("Varna")) {
            double coffee = 0.45;
            double water = 0.70;
            double beer = 1.10;
            double sweets = 1.35;
            double peanuts =1.55;

            if (product.equals("coffee")){
                java.lang.System.out.println(coffee * count);
            }else if (product.equals("water")){
                java.lang.System.out.println(water * count);
            }else if (product.equals("beer")){
                java.lang.System.out.println(beer * count);
            }else if (product.equals("sweets")){
                java.lang.System.out.println(sweets * count);
            }else if (product.equals("peanuts")){
                java.lang.System.out.println(peanuts * count);
            }
        }

      }
}