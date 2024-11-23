using System;
using System.Threading;

namespace Ex4MultipleThreads
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            var threadRequests = new Thread(MakingRequests);
            var threadDB = new Thread(AccessingDatabase);
            var threadOperations = new Thread(Operations);

            threadRequests.Start();
            threadDB.Start();
            threadOperations.Start();
        }

        static void MakingRequests()
        {
            Console.WriteLine("Making requests started using Thread 1");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Making requests: {i}");
                Console.WriteLine(i);
            }

            Console.WriteLine("Making requests ended using Thread 1");
        }

        static void AccessingDatabase()
        {
            Console.WriteLine("Access database started using Thread 2");

            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Access database: {i}");

                if (i == 3)
                {
                    Console.WriteLine("Performing the database operation started");
                    Thread.Sleep(1000);
                    Console.WriteLine("Performing the database operation finished");
                }
            }

            Console.WriteLine("Access database eneded using Thread 2");
        }

        static void Operations()
        {
            Console.WriteLine("Operations started using Thread 3");
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"Operations: {i}");
            }

            Console.WriteLine("Operations ended using Thread 3");
        }
    }
}