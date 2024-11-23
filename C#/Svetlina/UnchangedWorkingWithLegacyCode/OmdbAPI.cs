using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using Microsoft.Extensions.Configuration;

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
            Console.WriteLine(appSettings);

            ApiOmdbKey = appSettings["ApiOmdbKey"];
		}

        public static async Task<OmdbSearchResults> FindMovies(string movieTitle)
        {
            //async Task<OmdbSearchResults> Json()
            //{
            //    HttpResponseMessage response = await new HttpClient()
            //        .GetAsync($"https://www.omdbapi.com/?s={movieTitle}" +
            //    //              $"&apikey=<placeYourApiKeyHere");
            //                    $"&apikey=17498d05");

            //    response.EnsureSuccessStatusCode();
            //    string json = await response.Content.ReadAsStringAsync();
            //    return JsonSerializer.Deserialize<OmdbSearchResults>(json);
            //}

            //OmdbSearchResults imdbMatchingMovies = Json().Result;
            //return imdbMatchingMovies;


            string responseJson = await new HttpClient()
                .GetStringAsync($"{OmdbAPIUrl}?s={movieTitle}&apikey={ApiOmdbKey}");

            return JsonSerializer.Deserialize<OmdbSearchResults>(responseJson);
        }

        public static async Task<OmdbMovie> GetMovieDetails(string imdbId)
        {
            //async Task<OmdbMovie> Json()
            //{
            //    HttpResponseMessage response = await new HttpClient()
            //        .GetAsync($"https://www.omdbapi.com/?i={imdbId}" +
            //    //              $"&apikey=<placeYourApiKeyHere");
            //                    $"&apikey=17498d05");

            //    response.EnsureSuccessStatusCode();
            //    string json = await response.Content.ReadAsStringAsync();

            //    return JsonSerializer.Deserialize<OmdbMovie>(json);
            //}

            //return Json();

            string responseJson = await new HttpClient().GetStringAsync($"{OmdbAPIUrl}?i={imdbId}&apikey={ApiOmdbKey}");

            return JsonSerializer.Deserialize<OmdbMovie>(responseJson);
                
        }

    }
}

