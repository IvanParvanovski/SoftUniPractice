import java.util.Scanner;

public class MetricConventor {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double number = Double.parseDouble(scanner.nextLine());
        String enter = scanner.nextLine();
        String leave = scanner.nextLine();
        double meterConventor = 0;
        double meterConventorout = 0;

        if ("m".equalsIgnoreCase(enter)){
            meterConventor = number;
        }else if ("mm".equalsIgnoreCase(enter)){
            meterConventor = number / 1000;
        }else if ("cm".equalsIgnoreCase(enter)){
            meterConventor = number / 100;
        }else if ("mi".equalsIgnoreCase(enter)){
            meterConventor = number / 0.000621371192;
        }else if ("in".equalsIgnoreCase(enter)) {
            meterConventor = number / 39.3700787;
        }else if ("km".equalsIgnoreCase(enter)) {
            meterConventor = number * 1000;
        }else if ("ft".equalsIgnoreCase(enter)) {
            meterConventor = number / 3.2808399;
        }else if ("yd".equalsIgnoreCase(enter)) {
            meterConventor = number / 1.0936133;
        }
        if ("m".equalsIgnoreCase(leave)){
            meterConventorout = meterConventor;
        }else if ("mm".equalsIgnoreCase(leave)){
            meterConventorout = meterConventor * 1000;
        }else if ("cm".equalsIgnoreCase(leave)){
            meterConventorout = meterConventor * 100;
        }else if ("mi".equalsIgnoreCase(leave)){
            meterConventorout = meterConventor * 0.000621371192;
        }else if ("in".equalsIgnoreCase(leave)) {
            meterConventorout = meterConventor * 39.3700787;
        }else if ("km".equalsIgnoreCase(leave)) {
            meterConventorout = meterConventor / 1000;
        }else if ("ft".equalsIgnoreCase(leave)) {
            meterConventorout = meterConventor * 3.2808399;
        }else if ("yd".equalsIgnoreCase(leave)) {
            meterConventorout = meterConventor * 1.0936133;
        }
        System.out.printf("%.8f", meterConventorout);
    }
}
