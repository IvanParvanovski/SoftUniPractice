import java.util.Scanner;

public class Disspanser {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int maxWater = Integer.parseInt(scanner.nextLine());
        String typeOfWater = scanner.nextLine();
        int sumOfWater = 0;

        while (sumOfWater <= maxWater || typeOfWater.equalsIgnoreCase("Stop")) {
            if (typeOfWater.equalsIgnoreCase("Small")) {
                sumOfWater += 50;
            }

            if (typeOfWater.equalsIgnoreCase("Medium")) {
                sumOfWater += 100;
            }

            if (typeOfWater.equalsIgnoreCase("Big")) {
                sumOfWater += 150;
            }

            typeOfWater = scanner.nextLine();

            if(typeOfWater.equalsIgnoreCase("Stop")){
                break;
            }
        }

        if (sumOfWater > maxWater){
            System.out.println("Your cup is full.");
        }else
            System.out.println("Your Water is: " + sumOfWater);
    }
}
