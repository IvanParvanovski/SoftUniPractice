import java.util.Scanner;

public class Ex5Hidrograma {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int counterrN = Integer.parseInt(scanner.nextLine());
        int procent = 0;
        double p1 = 0;
        double p2 = 0;
        double p3 = 0;
        double p4 = 0;
        double p5 = 0;

        for (int i = 0; i < counterrN ; i++){
            int number = Integer.parseInt(scanner.nextLine());

            if (number < 200){
                p1++;
            }
            if (number >= 200 && number <= 399){
                p2++;
            }

            if (number >= 400 && number <= 599 ){
                p3++;
            }

            if (number >= 600 && number <= 799){
                p4++;
            }

            if (number >= 800 && number <= 1000){
                p5++;
            }
        }

         double prP1 = p1  / counterrN * 100;
         double prP2 =  p2  / counterrN * 100;
         double prP3 = p3 / counterrN * 100;
         double prP4 = p4  / counterrN * 100;
         double prP5 = p5  / counterrN * 100;



        System.out.printf("%.2f%%\n",prP1);
        System.out.printf("%.2f%%\n",prP2);
        System.out.printf("%.2f%%\n",prP3);
        System.out.printf("%.2f%%\n", prP4);
        System.out.printf("%.2f%%\n", prP5);


    }
}
