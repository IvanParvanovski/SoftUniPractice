using System.Text.Json.Serialization;

namespace MovieRentals
{
    public class OmdbMovie
    {
        public string Title { get; set; }
        public string Year { get; set; }
        public string Director { get; set; }
        public string Genre { get; set; }

        [JsonPropertyName("imdbRating")]
        public string ImdbRating { get; set; }
    }
}
