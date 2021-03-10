import java.util.Scanner;

public class Bakery {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = Integer.parseInt(scanner.nextLine());

        boolean eggs = false;
        boolean flour = false;
        boolean sugar = false;

        for (int i = 1; i <= n ; i++){
            String product = scanner.nextLine();
            while (!product.equalsIgnoreCase("Bake!")){
                if(product.equalsIgnoreCase("sugar")){
                    sugar = true;
                } else if (product.equalsIgnoreCase("flour")){
                    flour = true;
                } else if (product.equalsIgnoreCase("eggs")){
                    eggs = true;
                }
                product = scanner.nextLine();
            }

            if (eggs && flour && sugar ){
                 eggs = false;
                 flour = false;
                 sugar = false;

                System.out.printf("Baking batch number %d...%n", i);
            }else {
                i--;
                System.out.println("The batter should contain flour, eggs and sugar!");
            }
        }
    }
}
