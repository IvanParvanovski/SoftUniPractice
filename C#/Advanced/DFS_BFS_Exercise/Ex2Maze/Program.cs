using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Ex2Maze
{
    internal class Program
    {
        public static char[,] labyrinth;
        public static Point startPoint = new Point(-1, -1);

        public static void Main(string[] args)
        {
            ReadLabyrinth();
            
            string result = FindShortestPathToExit();

            if (result == "")
            {
                Console.WriteLine("Start is at the exit.");
            }
            else if (result == null)
            {
                Console.WriteLine("No exit!");
            }
            else
            {
                Console.WriteLine($"Shortest exit: {string.Join("", result.Reverse())}");
            }
        }

        static void ReadLabyrinth()
        {
            int width = int.Parse(Console.ReadLine()!);
            int height = int.Parse(Console.ReadLine()!);

            labyrinth = new char[height, width];

            for (int row = 0; row < height; row++)
            {
                string currentRow = Console.ReadLine()!;
                for (int col = 0; col < width; col++)
                {
                    labyrinth[row, col] = currentRow[col];

                    if (currentRow[col] == 's')
                    {
                        startPoint.X = col;
                        startPoint.Y = row;
                    }
                }
            }
        }

        static string FindShortestPathToExit()
        {
            if (!IsStartPointValid())
            {
                return null;
            }

            Queue<Point> queue = new Queue<Point>();
            queue.Enqueue(startPoint);

            while (queue.Count > 0)
            {
                var currentPoint = queue.Dequeue();

                if (IsExit(currentPoint))
                {
                    return TracePathBack(currentPoint);
                }

                TryDirection(queue, currentPoint, "U", 0, -1);
                TryDirection(queue, currentPoint, "R", 1, 0);
                TryDirection(queue, currentPoint, "D", 0, 1);
                TryDirection(queue, currentPoint, "L", -1, 0);
            }

            return null;
        }

        static string TracePathBack(Point currentCell)
        {
            StringBuilder sb = new StringBuilder();

            while (currentCell.PreviousPoint != null)
            {
                sb.Append(currentCell.Direction);
                currentCell = currentCell.PreviousPoint;
            }

            return sb.ToString();
        }

        static void TryDirection(Queue<Point> queue, Point sp, string direction, int deltaX, int deltaY)
        {
            int newX = sp.X + deltaX;
            int newY = sp.Y + deltaY;

            if (labyrinth[newY, newX] == '*' ||
                newX >= labyrinth.GetLength(1) ||
                newY >= labyrinth.GetLength(0) ||
                newX < 0 || newY < 0)
            {
                return;
            }

            labyrinth[newY, newX] = 's';
            
            Point newPoint = new Point(newX, newY);
            newPoint.PreviousPoint = sp;
            newPoint.Direction = direction;

            queue.Enqueue(newPoint);
        }

        static bool IsStartPointValid()
        {
            return startPoint.X != -1 && startPoint.Y != -1;
        }

        static bool IsExit(Point point)
        {
            return point.X == labyrinth.GetLength(1) - 1 ||
                   point.X == 0 ||
                   point.Y == labyrinth.GetLength(0) - 1 ||
                   point.Y == 0;
        }
    }
}