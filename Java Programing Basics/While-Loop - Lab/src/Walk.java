import java.util.Scanner;

public class Walk {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int steps = Integer.parseInt(scanner.nextLine());


        while (steps >= 10000){
            steps = Integer.parseInt(scanner.nextLine());
            System.out.println("Goal reached! Good job!");
        }


        while (steps < 10000){
            String command = scanner.nextLine();

            if (command.equalsIgnoreCase("GoingHome")){
                steps = Integer.parseInt(scanner.nextLine());
                double stepsLeft = 10000 - steps;
                System.out.printf("%.2f more steps to reach goal.", stepsLeft);
            }

            steps = Integer.parseInt(command);
        }


    }
}
