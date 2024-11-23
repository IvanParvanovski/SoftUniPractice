using System;

namespace MovieRentals
{
    public class MovieRentalApp
    {
        static void Main()
        {
            Console.WriteLine("-----------------------------------------");
            Console.WriteLine("-------- Movie Rental :: Welcome --------");
            Console.WriteLine("-----------------------------------------");

            while (true)
            {
                Console.WriteLine();
                Console.Write("Enter movie title (e.g. Spider-Man): ");

                string movieTitle = Console.ReadLine();
                
                if (movieTitle == "")
                {
                    Console.WriteLine("Goodbye.");
                    return;
                }

                ShowMovieSearchingResults(movieTitle);
            }
        }

        private static void ShowMovieSearchingResults(string movieTitle)
        {
            OmdbSearchResults matchingMovies = OmdbAPI.FindMovies(movieTitle).Result;

            if (matchingMovies.Response == "False")
            {
                Console.WriteLine("No movies found. Try again.");
                return;
            }
            
            Console.WriteLine();
            Console.WriteLine("Found {0} matching movies in OMDb.", matchingMovies.Search.Length);

            foreach (OmdbSearchResult movie in matchingMovies.Search)
            {
                Console.WriteLine();
                ShowMovieInfo(movie);
            }
        }

        private static void ShowMovieInfo(OmdbSearchResult movie)
        {
            OmdbMovie omdbMovie = OmdbAPI.GetMovieDetails(movie.ImdbID).Result;
            decimal price = MoviePricer.CalculatePrice(omdbMovie.ImdbRating);

            Console.WriteLine($"IMDB Id: {movie.ImdbID}");
            Console.WriteLine($"Title: {movie.Title}");
            Console.WriteLine($"Year: {movie.Year}");
            Console.WriteLine($"Raiting: {omdbMovie.ImdbRating}");
            Console.WriteLine($"Price: ${price:f2}");
        }
    }
}
