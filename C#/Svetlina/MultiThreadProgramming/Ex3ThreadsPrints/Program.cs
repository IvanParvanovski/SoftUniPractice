using System;
using System.Threading;

namespace Ex3ThreadsPrints
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            var workerThread = new Thread(PrintWorker);
            workerThread.Start();

            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"Main thread: {i}");
                Thread.Sleep(200);
            }
        }

        static void PrintWorker()
        {
            for (int i = 11; i < 20; i++)
            {
                Console.WriteLine($"Worker thread: {i}");
                Thread.Sleep(1000);

            }

        }
    }
}
