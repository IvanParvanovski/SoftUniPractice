using System.Text.Json.Serialization;

namespace MovieRentals
{
    public class OmdbSearchResults
    {
        public OmdbSearchResult[] Search { get; set; }
        public string Response { get; set; }
    }

    public class OmdbSearchResult
    {
        public string Title { get; set; }
        public string Year { get; set; }

        [JsonPropertyName("imdbID")]
        public string ImdbID { get; set; }
    }
}
