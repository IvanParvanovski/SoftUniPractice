namespace SynchronizationPrimitivesMutex
{
    public class Program
    {
        static Mutex mutex = new Mutex();

        public static void Main(string[] args)
        {
            for (int i = 0; i < 5; i++)
            {
                Thread thread = new Thread(DoWork);
                thread.Start(i);
            }

            Console.ReadLine();
        }

        static void DoWork(object threadId)
        {
            Console.WriteLine($"Thread {threadId} is trying to enter the critical section.");

            try
            {
                mutex.WaitOne();
                Console.WriteLine($"Thread {threadId} has entered the critical section and is doing some work.");
                Thread.Sleep(2000);
            }
            finally
            {
                mutex.ReleaseMutex();
                Console.WriteLine($"Thread {threadId} has exited the critical section.");
            }
        }
        

    }
}