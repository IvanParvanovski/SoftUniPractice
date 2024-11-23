using System;

namespace MovieRentals
{
    public class MoviePricer
    {
        public static decimal CalculatePrice(string imdbRating)
        {
            decimal price = 3.95m;
            double rating;

            try
            {
                rating = double.Parse(imdbRating);
            }
            catch (Exception)
            {
                rating = 5.0;
            }

            if (rating < 4.0)
            {
                price -= 1.0m;
            }
            else if (rating > 7.0)
            {
                price += 1.0m;
            }

            return price;
        }
    }
}
