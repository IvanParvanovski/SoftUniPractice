using System;

namespace BasicArrayList
{
    class StartUp
    {
        static void Main(string[] args)
        {
            // Write the solutions in ArrayList.cs

            ArrayList shopingList = new ArrayList();
            
            shopingList.Add(4);
            shopingList.Add(2);
            shopingList.Add(4);
            shopingList.Add(4);
            shopingList.Add(3);
            shopingList.Add(8);

            // Console.WriteLine(shopingList.CountFreePositions());
            shopingList.Cut(3);
            // Console.WriteLine(shopingList.CountFreePositions());
            
            Console.WriteLine(shopingList.Change(10, 5));
            Console.WriteLine(shopingList);
        }
    }
}
