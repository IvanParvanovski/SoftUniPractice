import java.util.Scanner;

public class TradeCommision {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String city = scanner.nextLine();
        double sells = Double.parseDouble(scanner.nextLine());
        double commision1 = -1.0;

        if (city.equals("Sofia")) {
            if (sells >= 0 && sells <= 500) {
                 commision1 = 0.05;
            } else if (sells >= 500 && sells < 1000) {
                 commision1 = 0.07;
            } else if (sells >= 1000 && sells < 10000) {
                 commision1 = 0.08;
            } else if (sells > 10000) {
                 commision1 = 0.12;
            }
        }if (city.equals("Varna")) {
            if (sells >= 0 && sells <= 500) {
                 commision1 = 0.045;
            } else if (sells > 500 && sells <= 1000) {
                 commision1 = 0.075;
            } else if (sells > 1000 && sells < 10000) {
                 commision1 = 0.10;
            } else if (sells > 10000) {
                 commision1 = 0.13;
            }
        }if (city.equals("Plovdiv")){
            if (sells > 0 && sells < 500){
                 commision1 = 0.055;
            }else if (sells > 500 && sells <= 1000){
                 commision1 = 0.08;
            }else if (sells > 1000 && sells < 10000){
                 commision1 = 0.12;
            }else if (sells > 10000){
                 commision1 = 0.145;
            }
        }
        if (commision1 >= 0){
        System.out.printf("%.2f", sells * commision1);
        }else
            System.out.println("error");
    }
}
