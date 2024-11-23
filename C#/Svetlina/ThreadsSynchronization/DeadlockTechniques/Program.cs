namespace DeadlockTechniques
{
    public class Program
    {
        static object obj1 = new object();
        static object obj2 = new object();

        public static void Main(string[] args)
        {
            Thread t1 = new Thread(new ThreadStart(Deadlock1));
            Thread t2 = new Thread(new ThreadStart(Deadlock2));
            t1.Start();
            t2.Start();

        }

        public static void Deadlock1()
        {
            lock (obj1)
            {
                Console.WriteLine("Thread 1 got locked.");
                Thread.Sleep(500);

                lock (obj2)
                {
                    Console.WriteLine("Thread 2 got locked");
                }
            }
        }

        public static void Deadlock2()
        {
            lock (obj2)
            {
                Console.WriteLine("Thread 2 got locked.");
                Thread.Sleep(500);

                lock (obj1)
                {
                    Console.WriteLine("Thread 1 got locked.");
                }
            }


        }
    }
}