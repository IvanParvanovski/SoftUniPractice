using System;

namespace Ex1Dates
{
    public class DateCounter
    {
        private string _firstDate;
        private string _secondDate;
        
        public string FirstDate
        {
            get => _firstDate;
            set => _firstDate = value;
        }

        public string SecondDate
        {
            get => _secondDate;
            set => _secondDate = value;
        }

        public DateCounter(string firstDate, string secondDate)
        {
            this.FirstDate = firstDate;
            this.SecondDate = secondDate;
        }

        public int CalculateDifference()
        {
            DateTime firstDate = DateTime.Parse(
                this._firstDate,
                System.Globalization.CultureInfo.InvariantCulture
            );

            DateTime secondDate = DateTime.Parse(
                this._secondDate,
                System.Globalization.CultureInfo.InvariantCulture
            );

            return Math.Abs((firstDate - secondDate).Days);
        }
    }
}