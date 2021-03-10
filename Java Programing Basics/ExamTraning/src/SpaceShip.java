import java.util.Scanner;

public class SpaceShip {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double shirina = Double.parseDouble(scanner.nextLine());
        double duljina = Double.parseDouble(scanner.nextLine());
        double visochina = Double.parseDouble(scanner.nextLine());
        double srednaVisch = Double.parseDouble(scanner.nextLine());

        double spaceShip = shirina * duljina * visochina;
        double austrounautRoom = (srednaVisch + 0.40) * 2 * 2;
        double place = spaceShip / austrounautRoom;
        double numAust = Math.floor(place);

        if (numAust <= 10 && place >= 3){
            System.out.printf("The spacecraft holds %.0f astronauts.", numAust);
        }

        if (numAust > 10){
            System.out.println("The spacecraft is too big.");
        }
        if (numAust < 3){
            System.out.println("The spacecraft is too small.");
        }





    }
}
