namespace Traverse
{
    public class SumOfCoins
    {
        public static void Main(string[] args)
        {
            List<int> coins = new List<int>();
            int target = int.Parse(Console.ReadLine());
            coins = coins.OrderByDescending(x => x).ToList();
            List<int> result = new List<int>();

            for (int i = 0; i < coins; i++)
            {

            }
        }
    }
}
