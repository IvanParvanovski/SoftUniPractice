namespace ShuffleString
{
    public class Program
    {
        public static void Main(string[] args)
        {
            string originalStr = "codeleet";
            char[] newStr = new char[originalStr.Length];

            var indices = new int[] {4, 5, 6, 7, 0, 2, 1, 3};


            for (int i = 0; i < originalStr.Length; i++)
            {
                newStr[indices[i]] = originalStr[i];
            }

            Console.WriteLine(string.Join("", newStr));
        }
    }
}