import java.util.Scanner;

public class Ex4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int kg = Integer.parseInt(scanner.nextLine());
        String food = scanner.nextLine();
        int currentEat = 0;


        while (!(food.equals("Adopted")) ){
            int currentFood = Integer.parseInt(food);
            currentEat += currentFood;
            food = scanner.nextLine();
        }

        if (currentEat > kg * 1000){
            int diff = currentEat - kg * 1000;
            System.out.printf("Food is not enough. You need %d grams more.", diff);
        }else {
            int diff = kg * 1000 - currentEat;
            System.out.printf("Food is enough! Leftovers: %d grams.", diff);
        }
    }
}
