using System;

namespace Recursion
{
  class Node
  {
    public Node Previous { get; set; }
    public Node Next { get; set; }
    public string Name { get; set; }

    public Node(Node previous, Node next, string name)
    {
      this.Previous = previous;
      this.Next = next;
      this.Name = name;
    }
  }
  
  internal class Program
  {
    static int[] square = new int[9];
    private static int[] visited = new int[9];
    
    public static void Main(string[] args)
    {
    }

    public static bool IsMagicSquare(int[,] matrix)
    {
      int N = 3;

      int sum = 0, sum2 = 0;

      for (int i = 0; i < N; i++)
      {
        sum = sum + matrix[i, i];
      }

      for (int i = 0; i < N; i++)
      {
        sum2 = sum2 + matrix[i, N - 1 - i];
      }

      if (sum != sum2)
      {
        return false;
      }

      for (int i = 0; i < N; i++)
      {
        int rowSum = 0;
        for (int j = 0; j < N; j++)
        {
          rowSum += matrix[i, j];
        }

        if (rowSum != sum)
        {
          return false;
        }
      }

      for (int i = 0; i < N; i++)
      {
        int colSum = 0;
        for (int j = 0; j < N; j++)
        {
          colSum += matrix[j, i];
        }

        if (sum != colSum)
        {
          return false;
        }
      }

      return true;
    }
    
  }
}