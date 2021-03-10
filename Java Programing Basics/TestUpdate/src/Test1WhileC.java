import java.util.Scanner;

public class Test1WhileC {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int waterCup = Integer.parseInt(scanner.nextLine());
        int waterGet = 0;
        int i = 0;

        while (waterCup >=  waterGet){
            String type = scanner.nextLine();
            if (type.equalsIgnoreCase("Easy")){
                waterGet = waterGet + 50;
            }

            if (type.equalsIgnoreCase("Medium")) {
                waterGet = waterGet + 100;
            }

            if (type.equalsIgnoreCase("Hard")){
                waterGet = waterGet + 200;
            }
            i++;
        }

        if (waterCup < waterGet) {
            int diff = waterGet - waterCup;
            System.out.printf("%dml has been spilled.", diff);
        }else
            System.out.printf("The dispenser has been tapped %d times.", i);
        }

    }
