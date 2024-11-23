namespace Ex1ReserveSeat    
{
    public class Program
    {
        static bool reserveField;
        static object lockObject = new object();

        public static void Main(string[] args)
        {
            Thread thread1 = new Thread(Reserve);
            thread1.Start();

            Thread thread2 = new Thread(Reserve);
            thread2.Start();

            Reserve();

        }

        static void Reserve()
        {
            lock (lockObject)
            {
                if (!reserveField)
                {
                    Console.WriteLine("Reserved");
                    reserveField = true;
                }
            }
            
        }
    }
}