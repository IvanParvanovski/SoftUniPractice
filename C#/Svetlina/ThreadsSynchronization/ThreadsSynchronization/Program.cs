namespace ThreadsSyncrhonization
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Printer p = new Printer();

            Thread t1 = new Thread(new ThreadStart(p.Print));
            Thread t2 = new Thread(new ThreadStart(p.Print));

            t1.Start();
            t2.Start();
        }
    }

    public class Printer
    {
        public void Print()
        {
            lock (this)
            {
                for (int i = 1; i <= 5; i++)
                {
                    Thread.Sleep(100);
                    Console.WriteLine(i);
                }
            }
        }
    }
}
