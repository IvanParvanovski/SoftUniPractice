using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.Linq;

namespace Lists_MORE_EXERCISE_
{
    class SortMethods
    {
        /*
         * From StackOverflow
         * Heap - The fastest in this project
        */

        public void SelectionSort(int[] numberSequence)
        {
            for (int i = 0; i < numberSequence.Length; i++)
            {
                int min = i;
                for (int j = i + 1; j < numberSequence.Length; j++)
                    if (numberSequence[min] > numberSequence[j])
                        min = j;

                if (min != i)
                {
                    var lowerValue = numberSequence[min];
                    numberSequence[min] = numberSequence[i];
                    numberSequence[i] = lowerValue;
                }
            }
        }

        public void InsertionSort(int[] numberSequence)
        {
            for (int i = 0; i < numberSequence.Length; i++)
            {
                int item = numberSequence[i];
                int currentIndex = i;

                while (currentIndex > 0 && numberSequence[currentIndex - 1] > item)
                {
                    numberSequence[currentIndex] = numberSequence[currentIndex - 1];
                    currentIndex--;
                }

                numberSequence[currentIndex] = item;
            }
        }

        public void heapSort(int[] numberSequence)
        {
            int n = numberSequence.Length;

            // Build heap (rearrange array)
            for (int i = n / 2 - 1; i >= 0; i--)
                heapify(numberSequence, n, i);

            // One by one extract an element from heap
            for (int i = n - 1; i > 0; i--)
            {
                // Move current root to end
                int temp = numberSequence[0];
                numberSequence[0] = numberSequence[i];
                numberSequence[i] = temp;

                // call max heapify on the reduced heap
                heapify(numberSequence, i, 0);
            }
        }

        public void heapify(int[] numberSequence, int n, int i)
        {
            int largest = i; // Initialize largest as root
            int l = 2 * i + 1; // left = 2*i + 1
            int r = 2 * i + 2; // right = 2*i + 2

            // If left child is larger than root
            if (l < n && numberSequence[l] > numberSequence[largest])
                largest = l;

            // If right child is larger than largest so far
            if (r < n && numberSequence[r] > numberSequence[largest])
                largest = r;

            // If largest is not root
            if (largest != i)
            {
                int swap = numberSequence[i];
                numberSequence[i] = numberSequence[largest];
                numberSequence[largest] = swap;

                // Recursively heapify the affected sub-tree
                heapify(numberSequence, n, largest);
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<int, Action> choicesFunctionalities = new Dictionary<int, Action>();
            choicesFunctionalities.Add(1, FirstOption);
            choicesFunctionalities.Add(2, SecondOption);
            choicesFunctionalities.Add(3, ThirdOption);
            choicesFunctionalities.Add(4, FourthOption);
            choicesFunctionalities.Add(5, FifthOption);
            choicesFunctionalities.Add(6, SixthOption);
            choicesFunctionalities.Add(7, SeventhOption);

            while (true)
            {
                int choice = GetOption();
                if (choice == 8) break;
                Action operation;

                if (!choicesFunctionalities.TryGetValue(choice, out operation))
                {
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("Invalid command!");
                    continue;
                }

                operation();
                Console.WriteLine();
            }
            Console.ForegroundColor = ConsoleColor.White;
        }

        private static int GetOption()
        {
            /*
             * 1. Print possible choices.
             * 2. Read user choice.
             * 3. Return user's choice.
             */

            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine("Please select one of the following options: \n");

            Console.ForegroundColor = ConsoleColor.Gray;
            Console.WriteLine("1. First    Option - Get Sum of the sequence, Max and Min number, and Average value.\n" +
                              "2. Second   Option - Get 100 Random numbers average value in range of two numbers.\n" +
                              "3. Third    Option - Get Sorted numbers in ascending order.\n" +
                              "4. Forth    Option - Get Secondary Max and Min number.\n" +
                              "5. Fifth    Option - Get Numbers power of two.\n" +
                              "6. Sixth    Option - Get The time of three functions. \n" +
                              "7. Seventh  Option - Get Is someone's egn valid. \n" +
                              "8. Eigth    Option - Exit. \n");
            int option;
            while (true)
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.Write("Your option is: ");
                Console.ForegroundColor = ConsoleColor.Green;
                string user_input = Console.ReadLine();
                if (Int32.TryParse(user_input, out option)) break;
                Console.ForegroundColor = ConsoleColor.DarkRed;
                Console.WriteLine("Invalid input try again!\n");
            }

            return option;
        }

        private static void FirstOption()
        {
            /*
             *  1. Read an integer number (num).
             *  2. Read num* numbers and save them in array.
             *  3. Print Sum, Min number, Max number, Average. 
             */

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("Please type the amount of numbers: ");
            Console.ForegroundColor = ConsoleColor.Green;
            int num = int.Parse(Console.ReadLine());
            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.WriteLine("Please type the numbers:");
            Console.ForegroundColor = ConsoleColor.Green;
            int[] numbers = (from number in Enumerable.Range(1, num) select int.Parse(Console.ReadLine())).ToArray();
                            
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("-- Your result --");
            Console.WriteLine($"Sum: {numbers.Sum()}\n" +
                              $"Min num: {numbers.Min()}\n" +
                              $"Max num: {numbers.Max()}\n" +
                              $"Average num: {numbers.Average():f2}");
        }

        private static void SecondOption()
        {
            /*  
             *   1. Read two variables (firstNum, secondNum).
             *   2. If "firstNum" > "secondNum" swap their values.
             *   3. Generate 10 Arrays containing 100 Random Numbers between N and M. 
             *   4. Print each array average value. 
             */

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("Please type the first number: ");
            Console.ForegroundColor = ConsoleColor.Green;
            int firstNum = int.Parse(Console.ReadLine());

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("Please type the second number: ");
            Console.ForegroundColor = ConsoleColor.Green;
            int secondNum = int.Parse(Console.ReadLine());

            Random random = new Random();

            int ARRAYS_AMOUNT_START = 0;
            int ARRAYS_AMOUNT_END = 10;

            int SEQUENCE_NUMBER_START = 1;
            int SEQUENCE_NUMBER_END = 100;

            string[] results = new string[ARRAYS_AMOUNT_END];

            if (ShouldSwap(firstNum, secondNum))
                SwapPositions(ref firstNum, ref secondNum);

            for (int i = ARRAYS_AMOUNT_START; i < ARRAYS_AMOUNT_END; i++)
                results[i] = $"{(from num in Enumerable.Range(SEQUENCE_NUMBER_START, SEQUENCE_NUMBER_END) select random.Next(firstNum, secondNum)).Average():f2}";

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("-- Your result --");
            Console.WriteLine(string.Join("\n", results));
        }

        private static void ThirdOption()
        {
            /*
             * 1. Initialize storage (List) with variable name (numbers).
             * 2. Loop until user type "-1".
             * 3. Sort the storage.
             * 4. Print the storate separated by space. 
             */

            List<int> numbers = new List<int>();
            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.WriteLine("Please type the numbers. To exit type '-1': ");
            Console.ForegroundColor = ConsoleColor.Green;
            while (true)
            {
                int num = int.Parse(Console.ReadLine());
                if (num == -1) break;
                numbers.Add(num);
            }

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("-- Your result --");
            numbers.Sort();
            Console.WriteLine(string.Join(" ", numbers));
        }

        private static void FourthOption()
        {
            /*
             * 1. Read the numbers separated by space.
             * 2. Get the Min and Max values of the sequence (funcMinNum) (funcMaxNum).
             * 3. Get the Min and Max values of Int32 (minNum = -2147483648) and (maxNum = 2147483648).
             * 4. Loop threw the sequence.
             * 5. Get the second smallest and biggest numbers.
             */

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("Please type the numbers separated by ', ': ");
            Console.ForegroundColor = ConsoleColor.Green;
            List<int> numbers = Console.ReadLine().Split(", ").Select(int.Parse).ToList();
            int funcMinNum = numbers.Min();
            int funcMaxNum = numbers.Max();

            int minNum = Int32.MaxValue;
            int maxNum = Int32.MinValue;

            foreach (int num in numbers)
            {
                if (num < minNum && num > funcMinNum)
                    minNum = num;

                if (num > maxNum && num < funcMaxNum)
                    maxNum = num;
            }

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("-- Your result --");
            Console.WriteLine($"Second Minimum num: {minNum}\n" +
                              $"Second Maximum num: {maxNum}");
        }


        // First Possibility
        //private static void FifthOption() => Console.WriteLine(string.Join(" ", Console.ReadLine().Split(',').Select(int.Parse).Where(x => IsStepOfTwo(x))));

        // Second Possibility
        private static void FifthOption()
        {
            /*
             * 1. Read numbers.
             * 2. Filter the numbers which are step of 2.
             * 3. Print filtered sequence.
             */

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("Please type the numbers separated by ', ': ");
            Console.ForegroundColor = ConsoleColor.Green;
            int[] numbers = Console.ReadLine().Split(", ").Select(int.Parse).ToArray();
            int[] numbersStepOfTwo = numbers.Where(x => IsStepOfTwo(x)).ToHashSet().ToArray();

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("-- Your result --");
            Console.WriteLine(string.Join(" ", numbersStepOfTwo)); ;
        }

        private static void SixthOption()
        {
            /*
             * 1. Initialize SortMethods object to have access of the sort methods.
             * 2. Initialize List (methods) to store the methods and easily operate with them.
             * 3. Generate a sequence with 100,000 numbers containing random numbers from -100 to 100.
             * 4. Calculate + Print each Method timing with (GetTiming).
             */

            SortMethods sortMethods = new SortMethods();
            Random random = new Random();
            List<Action<int[]>> methods = new List<Action<int[]>>() { sortMethods.heapSort,
                                                                      sortMethods.InsertionSort,
                                                                      sortMethods.SelectionSort, };
            int SEQUENCE_AMOUNT_OF_NUMBERS_START = 1;
            int SEQUENCE_AMOUNT_OF_NUMBERS_END = 100000;

            int SEQUENCE_NUMBER_START_RANGE = -100;
            int SEQUENCE_NUMBER_END_RANGE = 100;

            int[] seq = (from number in Enumerable.Range(SEQUENCE_AMOUNT_OF_NUMBERS_START, SEQUENCE_AMOUNT_OF_NUMBERS_END)
                         select random.Next(SEQUENCE_NUMBER_START_RANGE, SEQUENCE_NUMBER_END_RANGE)).ToArray();

            for (int i = 0; i < methods.Count(); i++)
                GetTiming(methods[i], seq.ToArray());
        }

        private static void SeventhOption()
        { 
            /*
             * 1. Initialize the table with powers and positions.
             * 2. Read user's egn
             * 3. Calculate egn with the formula (num[on specific position] * power) 
             * 4. Print if calculated control number is equal to the one in the user's egn.
             * 
             * --- Note ---
             * 5. There is a problem with a women egns.
             * 6. There are some wich sum is 10 or more.
             * 7. In most of the cases when the sum is 10 the contol number is 0.
             */

            Dictionary<int, int> positionPower = new Dictionary<int, int>()
            {
                { 0, 2 },
                { 1, 4 },
                { 2, 8 },
                { 3, 5 },
                { 4, 10 },
                { 5, 9 },
                { 6, 7 },
                { 7, 3 },
                { 8, 6 },
            };

            Console.ForegroundColor = ConsoleColor.DarkGray;
            Console.Write("Please type your egn: ");
            Console.ForegroundColor = ConsoleColor.Green;
            string egn = Console.ReadLine();

            int calculation = 0;
            for (int i = 0; i < 9; i++)
                calculation += positionPower[i] * int.Parse(egn[i].ToString());
            int fraction = calculation / 11;
            calculation -= fraction * 11;
            calculation = calculation >= 10 ? calculation % 10 : calculation;

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("-- Your result --");
            if (calculation == int.Parse(egn[9].ToString()))
                Console.WriteLine("valid");
            else
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                Console.WriteLine("invalid");
            }
        }
        private static void GetTiming(Action<int[]> func, int[] seq)
        {
            /*
             * 1. Start counting time with Stopwatch.StartNew()
             * 2. Execute function.
             * 3. Print executed time and reset. 
             */

            Stopwatch timing = Stopwatch.StartNew();
            func(seq);

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("-- Your result --");
            Console.WriteLine($"{func.Method.Name}: {timing.ElapsedMilliseconds}");
            timing.Stop();
        }

        private static void SwapPositions(ref int a, ref int b)
        {
            /*
             * 1. Use third variable to appropriate the value of the firstOne.
             * 2. Swap values.
             */

            int c = a;
            a = b;
            b = c;
        }

        private static bool ShouldSwap(int startNumber, int endNumber)
        {
            /*
             * 1. Is startNumber greater than the endNumber?
             * 2. Impossible to start increasing cycle with startRange greater than endRange.
             * 3. 15 (a) > 10 (b); a++ = endCycle 
             */

            return startNumber > endNumber;
        }

        private static bool IsStepOfTwo(int x)
        {
            /*
             * 1. X should not be 0
             * 2. Transfer to binary code and find the repetitive numbers.
             * 3. Check if the calculation is equal to 0.
             * 4. If it is "true" the number (x) is step of two.
             * 
             *    -- Example 1 --
             *    7 = 111
             *    6 = 110
             *        110 = 6 NOT POWER OF TWO
             *    
             *    -- Example 2 --
             *    
             *    4 = 100
             *    3 = 011
             *        000 = 0 POWER OF TWO
             */

            return (x != 0) && ((x & (x - 1)) == 0);
        }

    }
}
