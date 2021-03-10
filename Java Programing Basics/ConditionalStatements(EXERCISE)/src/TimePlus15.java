import java.util.Scanner;

public class TimePlus15 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int hours = Integer.parseInt(scanner.nextLine());
        int minutes = Integer.parseInt(scanner.nextLine());
        int sumtime = ((hours * 60) + (minutes + 15));
        int summin = sumtime % 60;
        int sumhours = sumtime / 60;


        if (sumhours == 24 && summin == 0 ) {
            System.out.printf("0:00");
        }else if (sumhours == 24 && summin < 10) {
            System.out.printf("0:0%d", summin);
        } else if (summin < 10) {
            System.out.printf("%d:0%d", sumhours, summin);

        }else if (sumhours == 24) {
            System.out.printf("0:%d", summin);
        } else
            System.out.printf("%d:%d", sumhours, summin);

    }
}
