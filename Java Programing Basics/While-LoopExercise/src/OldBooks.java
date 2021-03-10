import java.util.Scanner;

public class OldBooks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String bookName = scanner.nextLine();
        int library = Integer.parseInt(scanner.nextLine());
        int counter = 0;
        boolean found = false;
        while (!found && counter < library){
            found = bookName.equals(scanner.nextLine());
            counter++;

        }
        if (found) System.out.printf("You checked %d books and found it.", --counter);
        else System.out.printf("The book you search is not here!%nYou checked %d books.", counter);

    }
}