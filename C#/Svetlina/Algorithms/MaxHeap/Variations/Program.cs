namespace Variations
{
    public class Program
    {
        public static void Main(string[] args)
        {
            List<char> elements = new() { 'a', 'b', 'c' };

            Combine(elements, new char[2], 0, 2, 0);
            //Variate(elements,new char[elements.Count]);

        }

        //void Variate(List<char> elements, char[] current, int depth, bool[] used, int slots) 
        //{
        //    if (depth == slots)
        //    {
        //        Console.WriteLine(new string(current));
        //        return;
        //    }

        //    for (int i = 0; i < elements.Count; i++)
        //    {
        //        if (!used[i])
        //        {
        //            used[i] = true;
        //            current[depth] = elements[i];
        //            Variate(elements, current, depth + 1, used, slots);
        //            used =
        //        }

        //    }
        //}

        static void Combine(List<char> elements, char[] current, int depth, int slots, int start)
        {
            if (depth == slots)
            {
                Console.WriteLine(new string(current));
                return;
            }

            for (int i = start; i < elements.Count; i++)
            {
                current[depth] = elements[i];

                Combine(elements, current, depth + 1, slots, i + 1);   
            }

        }
    }
}