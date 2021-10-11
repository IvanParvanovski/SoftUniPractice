using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;

namespace Ex2Test
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] priceRatings = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            int entryPointIndex = int.Parse(Console.ReadLine());
            string expensiveOrCheap = Console.ReadLine();
            string itemsType = Console.ReadLine();

            int entryPoint = priceRatings[entryPointIndex];
            
            List<int> leftPart = new List<int>();
            for (int i = 0; i < entryPointIndex; i++)
            {
                int currentNum = priceRatings[i];

                if (expensiveOrCheap == "expensive")
                {
                    if (currentNum >= entryPoint)
                    {
                        if (itemsType == "positive" && currentNum >= 0)
                        {
                            leftPart.Add(currentNum);
                        } 
                        else if (itemsType == "negative" && currentNum < 0)
                        {
                            leftPart.Add(currentNum);
                        }
                        else if (itemsType == "all")
                        {
                            leftPart.Add(currentNum);
                        }
                    }
                } 
                else if (expensiveOrCheap == "cheap")
                {
                    if (currentNum < entryPoint)
                    {
                        if (itemsType == "positive" && currentNum >= 0)
                        {
                            leftPart.Add(currentNum);
                        } 
                        else if (itemsType == "negative" && currentNum < 0)
                        {
                            leftPart.Add(currentNum);
                        }
                        else if (itemsType == "all")
                        {
                            leftPart.Add(currentNum);
                        }
                    }
                }
            }

            List<int> rightPart = new List<int>();
            for (int i = entryPointIndex + 1; i < priceRatings.Length; i++)
            {
                int currentNum = priceRatings[i];

                if (expensiveOrCheap == "expensive")
                {
                    if (currentNum >= entryPoint)
                    {
                        if (itemsType == "positive" && currentNum >= 0)
                        {
                            rightPart.Add(currentNum);
                        } 
                        else if (itemsType == "negative" && currentNum < 0)
                        {
                            rightPart.Add(currentNum);
                        }
                        else if (itemsType == "all")
                        {
                            rightPart.Add(currentNum);
                        }
                    }
                } 
                else if (expensiveOrCheap == "cheap")
                {
                    if (currentNum < entryPoint)
                    {
                        if (itemsType == "positive" && currentNum >= 0)
                        {
                            rightPart.Add(currentNum);
                        } 
                        else if (itemsType == "negative" && currentNum < 0)
                        {
                            rightPart.Add(currentNum);
                        }
                        else if (itemsType == "all")
                        {
                            rightPart.Add(currentNum);
                        }
                    }
                }
            }

            int leftPartSum = leftPart.Sum();
            int rightPartSum = rightPart.Sum();

            if (leftPartSum >= rightPartSum)
            {
                Console.WriteLine($"Left - {leftPartSum}");
            }
            else
            {
                Console.WriteLine($"Right - {rightPartSum}");
            }
        }
    }
}