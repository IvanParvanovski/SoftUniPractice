import java.util.Scanner;

public class Ex3Graduation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String nameStudent = scanner.nextLine();
        double sum = 0;
        int levelOfClass = 1;
        int counter = 0;

        while (levelOfClass <= 12) {
            double grade = Double.parseDouble(scanner.nextLine());
            sum = sum + grade;
            double averagegrade = sum / 12;


            if (grade >= 4.0) {
                levelOfClass++;
                System.out.printf("%s graduated. Average grade: %.2f", nameStudent, averagegrade);
            }

            if (grade < 4.0) {
                counter++;
                System.out.printf("%s has been excluded at %d grade", nameStudent, counter);
            }

        break;}

    }
}



