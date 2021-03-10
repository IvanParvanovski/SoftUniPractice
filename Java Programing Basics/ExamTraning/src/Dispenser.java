import java.util.Scanner;

public class Dispenser {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int num = Integer.parseInt(scanner.nextLine());
        int count = 0;
        int water = 0;
        for (int i = 0; i < 5 ; i++){
            String button = scanner.nextLine();

            if (button.equals("Hard")){
                water += 200;
                count++;
            }

            if (button.equals("Medium")){
                water += 100;
                count++;
            }

            if (button.equals("Easy")){
                water += 50;
                count++;
            }
        }
        if (water <= num) {
            System.out.printf("The dispenser has been tapped %d times.", count);
        } else {
            int diff = num - water;
            System.out.printf("%dml has been spilled.", Math.abs(diff));
        }


        }
    }

