using System;

class Knapsack
{
    static void Main()
    {
        int[] weights = { 2, 3, 4, 5 };
        int[] values = { 3, 4, 5, 6 };
        int capacity = 5;

        int maxValue = KnapsackRecursive(weights, values, weights.Length, capacity);

        Console.WriteLine($"Maximum value that can be obtained: {maxValue}");
    }

    static int KnapsackRecursive(int[] weights, int[] values, int n, int capacity)
    {
        // Base case: if either no items or no capacity left
        if (n == 0 || capacity == 0)
            return 0;

        // If the weight of the nth item is more than the capacity, it cannot be included
        if (weights[n - 1] > capacity)
            return KnapsackRecursive(weights, values, n - 1, capacity);

        // Return the maximum of two cases:
        // 1. nth item included
        // 2. nth item not included
        return Math.Max(values[n - 1] + KnapsackRecursive(weights, values, n - 1, capacity - weights[n - 1]),
                        KnapsackRecursive(weights, values, n - 1, capacity));
    }
}