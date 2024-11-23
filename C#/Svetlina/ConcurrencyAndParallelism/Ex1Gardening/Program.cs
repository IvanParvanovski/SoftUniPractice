namespace Ex1Gardening
{
    public class Program
    {
        public static void Main(string[] args)
        {
            List<int> areaUnits = Enumerable.Range(0, 9).ToList();

            // Task Parallelism
            // One source, many different tasks sharing it

            Parallel.Invoke(
                () => Watering(areaUnits),
                () => Digging(),
                () => Weeding(areaUnits));

            Console.WriteLine(string.Join(" ", areaUnits));

        }

        public static void Watering(List<int> numbers)
        {
            // Data parallelism
            // Data - numbers - separated and the task all threads execute is the same

            Parallel.ForEach(numbers, i =>
            {
                if (i % 2 == 0)
                {
                    numbers[i]++;
                }
            });

            Console.WriteLine($"Worker Id: {Thread.CurrentThread.ManagedThreadId} - watering");
        }

        public static void Digging()
        {
            Console.WriteLine($"Worker Id: {Thread.CurrentThread.ManagedThreadId} - digging");
        }

        public static void Weeding(List<int> numbers)
        {
            numbers[1]--;
            Console.WriteLine($"Worker Id: {Thread.CurrentThread.ManagedThreadId} - weeding");
        }
    }
}