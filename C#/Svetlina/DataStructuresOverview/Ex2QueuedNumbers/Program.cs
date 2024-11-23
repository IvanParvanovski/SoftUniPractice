using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2QueuedNumbers
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Queue<int> numberQueue = new Queue<int>(Console.ReadLine().Split(',').Select(int.Parse));
            Queue<string> commandsStack = new Queue<string>(Console.ReadLine().Split(','));
            int result = 0; 

            while (commandsStack.Count != 0)
            {
                int number = numberQueue.Dequeue();
                string command = commandsStack.Dequeue().Trim();

                switch (command)
                {
                    case "Add":
                        result += number;
                        break;
                    case "Subtract":
                        result -= number;
                        break;
                    default:
                        numberQueue.Enqueue(number);
                        break;
                }
            }

            Console.WriteLine(result);
            Console.WriteLine(string.Join(" ", numberQueue));
        }
    }
}
