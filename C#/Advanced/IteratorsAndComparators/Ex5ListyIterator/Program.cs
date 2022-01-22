using System;
using System.Linq;

namespace Ex5ListyIterator
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            ListyIterator listyIterator = new ListyIterator(new object[0]);
            
            while (true)
            {
                string command = Console.ReadLine();

                if (command == "END")
                {
                    break;
                }

                switch (command)
                {
                    case "Create":
                        string[] commandTokens = command.Split(' ');
                        listyIterator = new ListyIterator(commandTokens.Skip(1).ToArray());
                        break;
                    
                    case "Print":
                        listyIterator.Print();
                        break;
                    
                    case "Move":
                        Console.WriteLine(listyIterator.Move());
                        break;
                    
                    case "HasNext":
                        Console.WriteLine(listyIterator.HasNext());
                        break;
                }
            }
        }
    }
}