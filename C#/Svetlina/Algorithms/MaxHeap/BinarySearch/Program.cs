namespace BinarySearch
{

    public class Program
    {
        public static void Main(string[] args)
        {

        }

        int BinarySearch(List<int> nums, int value)
        {
            int start = 0;
            int end = nums.Count - 1;

            while (start <= end)
            {
                int middle = start + (end - start) / 2;

                if (nums[middle] == value)
                {
                    return middle;
                }
                else if (value > nums[middle])
                {
                    start = middle + 1;
                }
                else
                {
                    end = middle - 1;
                }
            }

            return -1;
        }

    }
}