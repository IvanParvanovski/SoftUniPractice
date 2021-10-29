using System;

namespace Ex1
{
    public class DateDifferenceCalculator
    {
        public int daysDifference(DateTime date1, DateTime date2)
        {
            TimeSpan diff = date1.Subtract(date2);
            return diff.Days;
        }
    }
}