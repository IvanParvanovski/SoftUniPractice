import java.util.Scanner;

public class trip {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double tripMoney = Double.parseDouble(scanner.nextLine());
        double budget = Double.parseDouble(scanner.nextLine());
        int spendCounter = 0;
        int dayCounter = 1;

        while (tripMoney > budget){
            String action = scanner.nextLine();
            double dayMoney = Double.parseDouble(scanner.nextLine());

            if (action.equals("save")){
                budget += dayMoney;
                spendCounter = 0;
            }else if (action.equals("spend")){
                budget -= dayMoney;
                if (budget < 0){
                    budget = 0;
                }
                spendCounter++;

                if (spendCounter == 5){
                    System.out.println("You can't save the money.");
                    System.out.println(dayCounter);
                    return;
                }
            }
            dayCounter++;
        }

        System.out.printf("You saved the money for %d days.", (dayCounter - 1));
    }
}
