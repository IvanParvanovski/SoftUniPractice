import java.util.Scanner;

public class Scholarship {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double MoneyGetsBGN = Double.parseDouble(scanner.nextLine());
        double MiddlePoints = Double.parseDouble(scanner.nextLine());
        double MiniMoney = Double.parseDouble(scanner.nextLine());
        double MidPoints = (35 / 100.0) * MiniMoney;
        double MidPointsToZero = Math.floor(MidPoints);
        double ExcelentPoints = MiddlePoints * 25;
        double ExcelentToZero = Math.floor(ExcelentPoints);

        if (5.50 > MiddlePoints ){
            System.out.println("You cannot get a scholarship!");
        }else if (MiddlePoints >= 5.50 && MoneyGetsBGN < MiniMoney){
            System.out.printf("You get a Social scholarship %.0f BGN", MidPointsToZero);
        }else
            System.out.printf("You get a scholarship for excellent results %.0f BGN", ExcelentToZero);

    }

}