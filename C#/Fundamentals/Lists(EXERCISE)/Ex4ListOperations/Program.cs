using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex4ListOperations
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
            Dictionary<string, Action<List<int>, string[]>> commands = new Dictionary<string, Action<List<int>, string[]>>();
            commands.Add("Add", AddNumber);
            commands.Add("Insert", InsertNumber);
            commands.Add("Remove", RemoveNumberAtIndex);

            while (true)
            {
                string user_input = Console.ReadLine();

                if (user_input == "End")
                    break;

                string[] user_data = user_input.Split();
                string command = user_data[0];
                user_data = user_data.Skip(1).ToArray();

                Action<List<int>, string[]> value;
                if (commands.TryGetValue(command, out value))
                    value(numbers, user_data);
                else if (command == "Shift")
                    Shift(ref numbers, user_data);
            }
            Console.WriteLine(string.Join(" ", numbers));
        }
        public static void AddNumber(List<int> numbers, string[] data)
        {
            int number = int.Parse(data[0]);
            numbers.Add(number);
        }
        private static void InsertNumber(List<int> numbers, string[] data)
        {
            int item = int.Parse(data[0]);
            int index = int.Parse(data[1]);

            if (!IsIndexValid(index, numbers.Count()))
                Console.WriteLine("Invalid index");
            else
                numbers.Insert(index, item);
        }
        private static void RemoveNumberAtIndex(List<int> numbers, string[] data)
        {
            int index = int.Parse(data[0]);

            if (!IsIndexValid(index, numbers.Count()))
                Console.WriteLine("Invalid index");
            else
                numbers.RemoveAt(index);
        }
        private static void Shift(ref List<int> numbers, string[] data)
        {
            string side = data[0];
            int count = int.Parse(data[1]);

            switch (side)
            {
                case "left":
                    ShiftLeft(numbers, count);
                    break;
                case "right":
                    ShiftRight(numbers, count);
                    break;
            }

        }
        private static int ShiftLeft(List<int> numbers, int count)
        {
            if (count == 0)
                return 1;

            int element = numbers[0];
            numbers.RemoveAt(0);
            numbers.Add(element);
            return ShiftLeft(numbers, count - 1);
        }
        private static int ShiftRight(List<int> numbers, int count)
        {
            if (count == 0)
                return 1;

            int seqLastIndex = numbers.Count - 1;
            int element = numbers[seqLastIndex];
            numbers.RemoveAt(seqLastIndex);
            numbers.Insert(0, element);
            return ShiftRight(numbers, count - 1);
        }
        private static bool IsIndexValid(int index, int sequenceLength)
        {
            return index >= 0 && index < sequenceLength;
        }
    }
}
