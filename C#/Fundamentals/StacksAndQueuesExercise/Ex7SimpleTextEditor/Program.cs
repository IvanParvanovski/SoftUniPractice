using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Ex7SimpleTextEditor
{
    class Program
    {
        static void Main(string[] args)
        {
            int amountOfCommands = int.Parse(Console.ReadLine()!);
            Stack<char> result = new Stack<char>();
            
            string lastCommand = "0";
            string removedString = "";
            int amountOfElementsLastAdded = 0;

            
            for (int i = 0; i < amountOfCommands; i++)
            {
                string[] data = Console.ReadLine().Split();
                string command = data[0];

                switch (command)
                {
                    case "1":
                        lastCommand = "1";
                        amountOfElementsLastAdded = firstCommand(result, data[1]);
                        break;
                    case "2":
                        lastCommand = "2";
                        removedString = secondCommand(result, int.Parse(data[1]));
                        break;
                    case "3":
                        List<char> resultList = result.ToList();
                        resultList.Reverse();
                        Console.WriteLine(resultList[int.Parse(data[1]) - 1]);
                        break;
                    case "4":
                        if (lastCommand == "1")
                        {
                            removedString = secondCommand(result, amountOfElementsLastAdded);
                        }
                        else if (lastCommand == "2")
                        {
                            amountOfElementsLastAdded = firstCommand(result, removedString);
                        }
                        break;
                }
                Console.WriteLine(string.Join("", result));
                Console.WriteLine();
                Console.WriteLine();
            
            }
        }

        private static int firstCommand(Stack<char> result, string text)
        {
            foreach (char symbol in text)
            {
                result.Push(symbol);
            }

            return text.Length;
        }

        private static string secondCommand(Stack<char> result, int elementAmount)
        {
            Console.WriteLine(string.Join("", result));
            Console.WriteLine("IN ->" + elementAmount);
            StringBuilder removedString = new StringBuilder();
            for (int j = 0; j < elementAmount; j++)
            {
                removedString.Append(result.Pop());
            }

            return removedString.ToString();
        }
    }
}