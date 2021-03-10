import java.util.Scanner;

public class Graduation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String nameStudent = scanner.nextLine();
        double middleExcellent = 0;
        int levelOfClass = 1;

        while (levelOfClass <= 12){
            double grade = Double.parseDouble(scanner.nextLine());
            if(grade >= 4.0){
                levelOfClass++;
                middleExcellent += grade;
            }
        }
        double averagegrade = middleExcellent / 12;
        System.out.printf("%s graduated. Average grade: %.2f", nameStudent, averagegrade );
    }
}
