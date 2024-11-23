
namespace AlgorithmsFirstTerm
{
    class Program
    {
        public static void Main(string[] args)
        {
            int[] sequence = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();
            
            List<int> result = LongestZigzagSubsequence(sequence);
            Console.WriteLine(string.Join(' ', result));
        }

        static List<int> LongestZigzagSubsequence(int[] sequence)
        {
            int n = sequence.Length;

            if (n <= 2)
            {
                return sequence.ToList();
            }
            
            int[] inc = new int[n];
            int[] dec = new int[n];
            
            for (int i = 0; i < n; i++)
            {
                inc[i] = 1;
                dec[i] = 1;
            }

            int[] prevIncIndex = new int[n];
            int[] prevDecIndex = new int[n];

            for (int i = 0; i < n; i++)
            {
                prevIncIndex[i] = -1;
                prevDecIndex[i] = -1;
            }

            
            int endIndex = 0;
            int type = 0;
            
            for (int i = 1; i < n; i++)
            {
                for (int j = 0; j < i; j++)
                {
                    int current = sequence[i];
                    int previous = sequence[j];
                    if (current > previous && inc[i] < dec[j] + 1)
                    {
                        inc[i] = dec[j] + 1;
                        prevIncIndex[i] = j;
                    }
                    
                    else if (current < previous && dec[i] < inc[j] + 1)
                    {
                        dec[i] = inc[j] + 1;
                        prevDecIndex[i] = j;
                    }
                }
                
                if (inc[i] > dec[i] && inc[i] > inc[endIndex])
                {
                    endIndex = i;
                    type = 0;
                }
                else if (dec[i] > inc[i] && dec[i] > dec[endIndex])
                {
                    endIndex = i;
                    type = 1;
                }
            }

            List<int> zigzagSubsequence = new List<int>();
            int currentIndex = endIndex;
            while (currentIndex != -1)
            {
                zigzagSubsequence.Insert(0, sequence[currentIndex]);
                if (type == 0)
                {
                    currentIndex = prevIncIndex[currentIndex];
                }
                else
                {
                    currentIndex = prevDecIndex[currentIndex];
                }

                type = 1 - type;
            }

            return zigzagSubsequence;
        }
    }
}

