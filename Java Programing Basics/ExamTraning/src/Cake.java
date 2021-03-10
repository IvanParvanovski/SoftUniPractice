import java.util.Scanner;

public class Cake {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = Integer.parseInt(scanner.nextLine());
        int b = Integer.parseInt(scanner.nextLine());

        int area = a * b ;
        int count = 0;

        for (; count < area ; ){
            String peaces = scanner.nextLine();
            if (peaces.equals("STOP")){
                break;
            }
            int ioo = Integer.parseInt(peaces);
            count += ioo;
        }
        int diff = area - count;
        if (count > area){
            System.out.printf("No more cake left! You need %d pieces more.", Math.abs(diff));
        }else
            System.out.printf("%d pieces are left.", diff);

    }
}
