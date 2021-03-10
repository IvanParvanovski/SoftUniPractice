import java.util.Scanner;

public class SwimmingPool {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double RecordSeconds = Double.parseDouble(scanner.nextLine());
        double far = Double.parseDouble(scanner.nextLine());
        double TheFarfor1meter = Double.parseDouble(scanner.nextLine());

        double Distance = TheFarfor1meter * far;
        double Suprotivlenie = (far / 15);
        double OutAtack = Math.floor(Suprotivlenie);
        double Atack = OutAtack * 12.5;
        double SumTime = Atack + Distance;
        double TimeIfHeDont = SumTime - RecordSeconds;



        if (SumTime < RecordSeconds){
            System.out.printf("Yes, he succeeded! The new world record is " + "%.2f" +  " seconds." , SumTime);

        }else
            System.out.printf("No, he failed! He was " + "%.2f" + " seconds slower.",TimeIfHeDont );


    }
}
