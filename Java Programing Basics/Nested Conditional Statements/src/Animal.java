import java.util.Scanner;

public class Animal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String animal = scanner.nextLine();
        String type = "";

        switch (animal){
            case "crocodile":
            case "snake":
            case "tortoise":
                System.out.println("reptile");
                break;
            case "dog":
                System.out.println("mammal");
            default:
                System.out.println("unknown");
        }
    }
}
