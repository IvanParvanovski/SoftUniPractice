import java.util.Scanner;

public class Ex6Travell {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String destination = scanner.nextLine();


        while (!destination.equalsIgnoreCase("end") ) {
            double minBudget = Double.parseDouble(scanner.nextLine());

            double saving = 0;
            while (saving < minBudget) {
                saving += Double.parseDouble(scanner.nextLine());
            }

            System.out.printf("Going to %s!%n", destination);
            saving -= minBudget;
            destination = scanner.nextLine();

        }
    }
}

