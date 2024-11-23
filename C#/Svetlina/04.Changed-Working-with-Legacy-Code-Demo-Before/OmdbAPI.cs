using Microsoft.Extensions.Configuration;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace MovieRentals
{
    public class OmdbAPI
    {
        protected const string OmdbAPIUrl = "https://www.omdbapi.com/";
        protected static readonly string ApiOmdbKey;

        static OmdbAPI()
        {
            var appSettings = new ConfigurationBuilder()
                .AddJsonFile("appsettings.json").Build();
            System.Console.WriteLine(appSettings);

            ApiOmdbKey = appSettings["ApiOmdbKey"];
        }

        public static async Task<OmdbSearchResults> FindMovies(string movieTitle)
        {
            string responseJson = await new HttpClient()
                .GetStringAsync($"{OmdbAPIUrl}?s={movieTitle}&apikey={ApiOmdbKey}");

            return JsonSerializer.Deserialize<OmdbSearchResults>(responseJson);
        }

        public static async Task<OmdbMovie> GetMovieDetails(string imdbId)
        {
            string response = await new HttpClient()
                .GetStringAsync($"{OmdbAPIUrl}?i={imdbId}&apikey={ApiOmdbKey}");

            return JsonSerializer.Deserialize<OmdbMovie>(response);
        }
    }
}
