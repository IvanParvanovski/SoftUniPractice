using System;
using System.Collections.Generic;
using System.Threading;

namespace Ex4Boom
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            string message = Console.ReadLine();
            var myThread = new Thread(() => Boom(message));
            myThread.Start();
        }


        private static void Boom(string msg)
        {
            bool status = false;
            var numbers = new List<char>() { '1', '2', '3', '4', '5', '6', '7', '8', '9' };


            foreach (char symbol in msg)
            {
                if (numbers.Contains(symbol))
                {
                    status = true;
                    break;
                }
            }

            if (status)
            {
                Console.WriteLine("Boom");
            }
            else
            {
                Console.WriteLine("There are no bombs in the text.");
            }
        }
    }
}
