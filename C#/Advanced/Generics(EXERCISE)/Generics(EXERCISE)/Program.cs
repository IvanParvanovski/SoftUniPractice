using System;
using System.Linq;

namespace Generics_EXERCISE_
{
    class Program
    {
        const int INITIAL_CAPACITY = 5;
        static int[] numbers = {51, 47, 32, 61, 21};
        // static int[] numbers = {13, 18, 85, 90, 46};

        static void Main(string[] args)
        {
            int rotations = int.Parse(Console.ReadLine());
            string direction = Console.ReadLine();

            Console.WriteLine(String.Join(" ", RotateArray(rotations, direction)));
        }

        public static int[] RotateArray(int rotations, string direction)
        {
            for (int i = 0; i < rotations; i++)
            {
                int[] newArray = new int[INITIAL_CAPACITY];

                if (direction == "left")
                {
                    for (int k = 0; k < INITIAL_CAPACITY - 1; k++)
                    {
                        newArray[k + 1] = numbers[k];
                    }

                    newArray[0] = numbers[INITIAL_CAPACITY - 1];
                }
                else
                {
                    for (int k = 1; k < INITIAL_CAPACITY; k++)
                    {
                        newArray[k - 1] = numbers[k];
                    }

                    newArray[INITIAL_CAPACITY - 1] = numbers[0];
                }
                
                numbers = newArray;
            }

            return numbers;
        }
    }
}
