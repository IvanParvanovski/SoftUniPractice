import java.util.Scanner;

public class Exam {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int maxPoorGrades = Integer.parseInt(scanner.nextLine());
        int counterPoorGrades = 0;


        int counterAllTasks = 0;
        int scoreAllGrades = 0;
        String LastProblem = "";

        while (counterPoorGrades < maxPoorGrades) {
            String task = scanner.nextLine();
            if (task.equals("Enough")) {
                System.out.printf("Average score: %.2f%n", scoreAllGrades * 1.0 / counterAllTasks );
                System.out.printf("Number of problems: %d%n", counterAllTasks);
                System.out.printf("Last problem: %s", LastProblem);
                return;
            }
            int currentgrade = Integer.parseInt(scanner.nextLine());

            if (currentgrade <= 4) {
                counterPoorGrades++;
            }
            if (counterPoorGrades == maxPoorGrades) {
                System.out.printf("You need a break, %d poor grades.", counterPoorGrades);
            }

            counterAllTasks++;
            scoreAllGrades += currentgrade;
            LastProblem = task;


        }
    }
}
