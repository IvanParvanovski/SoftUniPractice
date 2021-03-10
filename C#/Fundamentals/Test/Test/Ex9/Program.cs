using System;

namespace Ex9
{
    class Program
    {
        static void Insert(ref int mask, int el)
        {
            mask |= (1 << el);
        }

        static void Main(string[] args)
        {
            int num = 0;
            
            
            for (int i = 0; i < 10; i++)
            {
                string isStudentHere = Console.ReadLine();
                
                if (isStudentHere == "Yes")
                    Console.WriteLine();
                else
                    Console.WriteLine();
            }
        }
    }
}