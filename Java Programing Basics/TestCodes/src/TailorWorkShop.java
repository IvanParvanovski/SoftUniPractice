import java.util.Scanner;

public class TailorWorkShop {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //Pravougulnik
        double a = Double.parseDouble(scanner.nextLine());
        double b = Double.parseDouble(scanner.nextLine());
        double RectAngleArea = (a + 0.6) * (b + 0.6);
        System.out.println(RectAngleArea);

        //Kvadrat
        double SquareArea = (a / 2) * (a / 2);
        System.out.println(SquareArea);

        //LEVA PRAVOUGULNIK
        double BGN = 7 * 1.85;
        //LEVA KVADRAT
        double BGN1 = 9 * 1.85;


        double n = Double.parseDouble(scanner.nextLine());

        //DOLARI
        double pokrifka1 = 7 * n * RectAngleArea;
        System.out.println(pokrifka1);
        double kareta1 = 9 * n * SquareArea;
        System.out.println(kareta1);
        //LEVA
        double pokrifka2 = BGN * n * RectAngleArea;
        System.out.println(pokrifka2);
        double kareta2 = BGN * n * SquareArea;
        System.out.println(kareta2);



    }
}
