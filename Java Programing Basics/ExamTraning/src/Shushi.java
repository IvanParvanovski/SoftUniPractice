import java.util.Scanner;

public class Shushi {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String typeShusi = scanner.nextLine();
        String restourant = scanner.nextLine();
        int numFood = Integer.parseInt(scanner.nextLine());
        String YorN = scanner.nextLine();
        double price = 0 * 0.0;
        double sum = 0 * 0.0;
        double sumFull = 0 * 0.0;

        if (restourant.equalsIgnoreCase("Sushi Zone") || restourant.equalsIgnoreCase("Sushi Time")
                || restourant.equalsIgnoreCase("Sushi Bar") || restourant.equalsIgnoreCase("Asian Pub")||
                restourant.equalsIgnoreCase("Sushi Zone ") || restourant.equalsIgnoreCase("Sushi Time ")
                || restourant.equalsIgnoreCase("Sushi Bar ") || restourant.equalsIgnoreCase("Asian Pub ")) {
            if (typeShusi.equalsIgnoreCase("sashimi")) {
                if (restourant.equalsIgnoreCase("Sushi Zone") || restourant.equalsIgnoreCase("Sushi Zone ")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.99;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.99;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Time") || restourant.equalsIgnoreCase("Sushi Time ")){
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 5.49;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 5.49;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Bar") || restourant.equalsIgnoreCase("Sushi Bar ")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 5.25;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 5.25;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Asian Pub") || restourant.equalsIgnoreCase("Asian Pub ")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.50;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.50;
                        sumFull = price * numFood;
                    }
                }
            }

            //Second

            if (typeShusi.equalsIgnoreCase("maki")) {
                if (restourant.equalsIgnoreCase("Sushi Zone") ||  restourant.equalsIgnoreCase("Sushi Zone ")){
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 5.29;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 5.29;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Time") || restourant.equalsIgnoreCase("Sushi Time ")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.69;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.69;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Bar") || restourant.equalsIgnoreCase("Sushi Bar ")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 5.55;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 5.55;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Asian Pub") || restourant.equalsIgnoreCase("Asian Pub ")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.80;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.80;
                        sumFull = price * numFood;
                    }
                }
            }


            //THIRD

            if (typeShusi.equalsIgnoreCase("uramaki")) {
                if (restourant.equalsIgnoreCase("Sushi Zone")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 5.99;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 5.99;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Time")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.49;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.49;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Bar")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 6.25;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 6.25;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Asian Pub")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.50;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.50;
                        sumFull = price * numFood;
                    }
                }
            }


            //Fourth

            if (typeShusi.equalsIgnoreCase("temaki")) {
                if (restourant.equalsIgnoreCase("Sushi Zone")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.29;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.29;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Time")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 5.19;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 5.19;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Sushi Bar")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 4.75;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 4.75;
                        sumFull = price * numFood;
                    }
                }

                if (restourant.equalsIgnoreCase("Asian Pub")) {
                    if (YorN.equalsIgnoreCase("Y")) {
                        price = 5.50;
                        sum = (price * numFood);
                        sumFull = (20 / 100.0 * sum) + sum;
                    } else {
                        price = 5.50;
                        sumFull = price * numFood;
                    }
                }
            }
            System.out.printf("Total price: %d lv.", (int) Math.ceil(sumFull));
        }else
            System.out.printf("%s is invalid restaurant!", restourant);
    }
}


