import java.awt.desktop.SystemSleepEvent;
import java.util.Scanner;

public class Choreography {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double steps = Integer.parseInt(scanner.nextLine());
        double dancers = Integer.parseInt(scanner.nextLine());
        double days = Integer.parseInt(scanner.nextLine());
        double sumOfSteps = ((steps / days) / steps );
        double PROCENT = sumOfSteps * 100;
        double ProcentUp = Math.ceil(PROCENT);
        double procentSteps = ProcentUp / dancers;


        if (PROCENT <= 13){
            System.out.printf("Yes, they will succeed in that goal! %.2f%%.", procentSteps);
        }else

            System.out.printf("No, They will not succeed in that goal! Required %.2f%% steps to be learned per day.", procentSteps);








    }
}
