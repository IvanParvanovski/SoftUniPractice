namespace SyncrhonizationPrimitivesMonitor
{
    public class Program
    {
        static readonly object tLock = new object();

        public static void Main(string[] args)
        {
            Thread[] Threads = new Thread[3];

            for (int i = 0; i < 3; i++)
            {
                Threads[i] = new Thread(new ThreadStart(PrintNumbers));
                Threads[i].Name = "Child " + i;
            }
            foreach (var t in Threads)
            {
                t.Start();
            }
        }

        public static void PrintNumbers()
        {
            Monitor.Enter(tLock);

            try
            {
                for (int i = 0; i < 5; i++)
                {
                    Console.WriteLine($"{Thread.CurrentThread.Name} - {i}");
                }
            }
            catch (SynchronizationLockException SyncEx)
            {

            }
            finally
            {
                Monitor.Exit(tLock);
            }
        }
    }
}