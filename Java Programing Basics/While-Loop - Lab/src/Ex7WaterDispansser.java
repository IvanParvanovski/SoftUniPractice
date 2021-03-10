import java.util.Scanner;

public class Ex7WaterDispansser {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int cupVolume = Integer.parseInt(scanner.nextLine());
        int Water = 0;
        int counter = 0;
        int max = Integer.MIN_VALUE;

        while (cupVolume >= Water) {
            String Button = scanner.nextLine();
            if (Button.equalsIgnoreCase("Easy")) {
                Water = 50;
            }
            if (Button.equalsIgnoreCase("Medium")) {
                Water = 100;

            }
            if (Button.equalsIgnoreCase("Hard")) {
                Water = 200;
                counter++;
            }
            counter++;

        }
        System.out.printf("The dispenser has been tapped %d times.", counter);



        while (Water > cupVolume){
        if (Water > cupVolume) {
            int waterSlipt = Water - cupVolume;
            System.out.printf("%dml has been spilled.", waterSlipt);
            break;
        }

        }

    }
}

