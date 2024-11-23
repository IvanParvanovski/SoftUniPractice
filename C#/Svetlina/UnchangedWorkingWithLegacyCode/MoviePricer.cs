using System;
namespace MovieRentals
{
	public class MoviePricer
	{
		public static decimal CalculatePrice(OmdbMovie movie)
		{
            decimal price = 3.95m;
			double rating;

			try
			{
                rating = double.Parse(movie.imdbRating);
            }
            catch (Exception ex)
			{
				rating = 5.0;
			}

		    if (rating < 4)
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

