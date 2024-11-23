using System;
using System.Threading;

namespace MultiThreadProgramming
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("hello");
            try
            {
                string msg = "msg";
                Thread t1 = new Thread(() => DoWork(msg));
            }
            catch (ArgumentNullException)
            {
                Console.WriteLine("Exception");
            }
        }

        static void DoWork(string msg)
        {
            Console.WriteLine(msg);
            throw new ArgumentNullException();
        }
    }
}
