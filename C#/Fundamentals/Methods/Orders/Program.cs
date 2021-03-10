namespace Orders
{
    using System;

    class Program
    {
        static void Main()
        {
            while (true)
            {
                Console.Write("Please type your command: ");
                string command = Console.ReadLine();
                string output = "";
                switch (command)
                {
                    case "on":
                        output = "Command is on...";
                        break;

                    case "off":
                        output = "Command is off...";
                        break;

                    case "exit":
                        return;
                }

                Console.WriteLine(output);
            }
        }

        static void increment(ref int num)
        {
            num++;
        }

        static void swap(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }

        static void GetIntLength(int num)
        {
            int counter = 0;


            while (true)
            {
                counter++;

                if (num < 10)
                    break;

                num /= 10;
                
            }
            Console.WriteLine(counter);
        }


    }
}
