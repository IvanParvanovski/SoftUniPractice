import java.util.Scanner;

public class FruitOrVegetables {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String meal = scanner.nextLine();

        if (meal.equals("banana") || meal.equals("cherry") || meal.equals("lemon") || meal.equals("grapes") || meal.equals("apple") || meal.equals("kiwi")){
            System.out.println("fruit");
        }else if (meal.equals("tomato") || meal.equals("cucumber") || meal.equals("pepper") || meal.equals("carrot")){
            System.out.println("vegetable");
        }else
            System.out.println("unknown");

    }
}
