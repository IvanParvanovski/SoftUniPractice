using System;
using System.Linq;
using System.Threading;

namespace Dealership
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            // Main colors
            const ConsoleColor optionMessageColor = ConsoleColor.White;
            const ConsoleColor optionColor = ConsoleColor.Green;
            const ConsoleColor menuColor = ConsoleColor.DarkCyan;
            int milliseconds = 3250;
     
            // Create the warehouse
            Console.ForegroundColor = optionMessageColor;
            Console.WriteLine("Please, type the name of your warehouse:");
            
            Console.ForegroundColor = optionColor;
            string warehouseName = Console.ReadLine();
            Console.WriteLine();

            Warehouse<string> warehouse = new Warehouse<string>(warehouseName, "randomId");

            string[] menu = 
            {
                "Welcome!",
                "These are the options you can select from:",
                " 1. --) Add a new car",
                " 2. --) Remove a car",
                " 3. --) Get the amount of cars",
                " 4. --) Repaint a car",
                " 5. --) Tuning a car",
                " 6. --) Test Drive your favourite model",
                " 7. --) Fill up the tank of a car",
                " 8. --) Show the cars",
                " 9. --) Show warehouse"
            };

            while (true)
            {
                // Display the menu and read the option
                Console.ForegroundColor = menuColor;
                Console.WriteLine(String.Join("\n", menu));

                Console.ForegroundColor = optionMessageColor;
                Console.WriteLine("Your option is: ");
            
                Console.ForegroundColor = optionColor;
                string option = Console.ReadLine();
                
                if (option == "End")
                {
                    break;
                }
                
                // Fulfill the user's option
                int optionNum = int.Parse(option ?? throw new InvalidOperationException());
                Console.WriteLine();
                
                switch (optionNum)
                {
                    case 1:
                        // Get model
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The model is: ");
            
                        Console.ForegroundColor = optionColor;
                        string model = Console.ReadLine();
                    
                        // Get horse power
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The horse power is: ");
            
                        Console.ForegroundColor = optionColor;
                        int horsePower = int.Parse(Console.ReadLine() ?? throw new InvalidOperationException());
                    
                        // Get color
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The color is: ");
            
                        Console.ForegroundColor = optionColor;
                        string color = Console.ReadLine();
                    
                        Car car = new Car(model, horsePower, color);
                        Console.WriteLine(warehouse.AddCar(car));
                        break;
                    case 2:
                        // Remove car
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The car model you want to remove is: ");
            
                        Console.ForegroundColor = optionColor;
                        string carModel = Console.ReadLine();

                        Console.WriteLine(warehouse.RemoveCar(carModel));
                        break;
                    case 3:
                        Console.WriteLine(warehouse.GetAmount());
                        break;
                    case 4:
                        // Get car model
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The model is: ");
            
                        Console.ForegroundColor = optionColor;
                        string carModelToRepaint = Console.ReadLine();
                        
                        // Get the new color
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The car new color is: ");
            
                        Console.ForegroundColor = optionColor;
                        string newColor = Console.ReadLine();
                        
                        Console.WriteLine(warehouse.RepaintCar(carModelToRepaint, newColor));
                        break;
                    case 5:
                        // Get car model
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The car model is: ");
            
                        Console.ForegroundColor = optionColor;
                        string carModelToTuning = Console.ReadLine();
                        
                        // Get car part
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The car part is: ");
            
                        Console.ForegroundColor = optionColor;
                        string carPart = Console.ReadLine();
                        
                        // Get horse power
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The added horse power is: ");
            
                        Console.ForegroundColor = optionColor;
                        int morePower = int.Parse(Console.ReadLine() ?? throw new InvalidOperationException());
                        
                        Console.WriteLine(warehouse.Tuning(carModelToTuning, carPart, morePower));
                        break;
                    case 6:
                        // Get car model
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The car model is: ");
            
                        Console.ForegroundColor = optionColor;
                        string carModelToDrive = Console.ReadLine();
                        
                        Console.WriteLine(warehouse.TestDrive(carModelToDrive));
                        break;
                    case 7:
                        // Get car model
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The car model is: ");
            
                        Console.ForegroundColor = optionColor;
                        string carModelToFill = Console.ReadLine();
                        
                        // Get amount
                        Console.ForegroundColor = optionMessageColor;
                        Console.WriteLine("The added fuel amount is: ");
            
                        Console.ForegroundColor = optionColor;
                        int fuelAmount = int.Parse(Console.ReadLine());
                        
                        Console.WriteLine(warehouse.RefuelCar(carModelToFill, fuelAmount));
                        break;
                    case 8:
                        Console.ForegroundColor = ConsoleColor.Cyan;

                        // Show the cars
                        foreach (Car vehicle in warehouse.OrderBy(x => x))
                        {
                            Console.WriteLine(vehicle);
                        }
                        
                        break;
                    case 9:
                        // Show warehouse
                        Console.WriteLine(warehouse.GetDisplayTable());
                        break;
                }
                Thread.Sleep(milliseconds);
            }
        }
    }
}