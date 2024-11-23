namespace Ex3
{
    public class Program
    {
        public static void Main(string[] args)
        {
            
        }

        public int MinSwitches(int[] bulbs)
        {
            int count = 0;
            int state = 0;

            foreach (int bulb in bulbs)
            {
                if ((state % 2 == 0 && bulb == 0) || (state % 2 == 1 && bulb == 1))
                {
                    count++;
                    state++; 
                }
            }

            return count;
        }
    }
}