namespace SynchronizationPrimitivesSemaphore
{
    public class Program
    {
        static Semaphore semaphore = new Semaphore(2, 3);

        public static void Main(string[] args)
        {
            for (int i = 1; i <= 5; i++)
            {
                new Thread(Enter).Start(i);
            }
        }

        static void Enter(object id)
        {
            Console.WriteLine(id + " wants to enter");

            semaphore.WaitOne();
            Console.WriteLine(id + " is in!");

            Thread.Sleep(1000 * (int)id);
            Console.WriteLine(id + " is leaving");

            semaphore.Release();

        }


    }    
}

