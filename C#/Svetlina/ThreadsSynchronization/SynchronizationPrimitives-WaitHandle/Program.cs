namespace SyncrhonizationPrimitivesWaitHandle
{
    public class Program
    {
        static WaitHandle[] waitHandles = new WaitHandle[]
        {
            new AutoResetEvent(false),
            new AutoResetEvent(false),
        };

        static ManualResetEvent waitHandle = new ManualResetEvent(false);


        public static void Main(string[] args)
        {
            //DateTime dt = DateTime.Now;
            //Console.WriteLine("Main thread is waiting for BOTH tasks to complete.");

            //ThreadPool.QueueUserWorkItem(new WaitCallback(DoTask), waitHandles[0]);
            //ThreadPool.QueueUserWorkItem(new WaitCallback(DoTask), waitHandles[1]);
            //WaitHandle.WaitAll(waitHandles);

            //Console.WriteLine($"Both tasks are completed (time waited={DateTime.Now - dt})");

            Thread waitThread = new Thread(WaitingThread);
            waitThread.Start();

            Console.WriteLine("Doing some work...");
            Thread.Sleep(2000);
            waitHandle.Set();

            Console.WriteLine("Main thread continues");

            waitThread.Join();
        }

        static void DoTask(Object state)
        {
            Random r = new Random();

            AutoResetEvent eventObj = (AutoResetEvent)state;
            int time = 1000 * r.Next(2, 10);
            Console.WriteLine($"Performing a task for {time} milliseconds.");
            Thread.Sleep(time);
            eventObj.Set();
        }

        static void WaitingThread()
        {
            Console.WriteLine("Waiting thread is waiting for the signal.");
            waitHandle.WaitOne();
            Console.WriteLine("Waiting thread received the signal and continues.");
        }
    }
}

