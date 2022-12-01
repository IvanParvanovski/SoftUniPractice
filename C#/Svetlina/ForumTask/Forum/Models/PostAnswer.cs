
namespace Forum.Models
{
    public class PostAnswer
    {
        public int Id { get; set; }
        public string AnswerContent { get; set; }
        public int PostId { get; set; }
        public Post Post { get; set; }

    }
}
