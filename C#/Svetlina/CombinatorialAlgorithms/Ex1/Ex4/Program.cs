using System.Linq;

namespace Ex4Fuel
{
    public class Program
    {
        public static void Main(string[] args)
        {
            double[] gas = { 1, 2 };
            double[] distance = { 2, 1 };
            Dictionary<int, double> proporions = new Dictionary<int, double>();
            List<int> indexes = new List<int>();
            
            for (int i = 0; i < gas.Length; i++)
            {
                if (!proporions.ContainsKey(i))
                {
                    proporions[i] = 0;
                }

                proporions[i] = gas[i] / distance[i];
            }

            var sortedProportions = proporions.OrderByDescending(kvp => kvp.Value).ToDictionary(kv => kv.Key, kv => kv.Value);
            double currentFuel = 0;

            foreach (var kvp in sortedProportions)
            {
                currentFuel += gas[kvp.Key];
                currentFuel -= distance[kvp.Key];
            }


            if (currentFuel >= 0)
            {
                Console.WriteLine(sortedProportions.First().Key);
            }
            else
            {
                Console.WriteLine(-1);
            }


        }
    }
} 