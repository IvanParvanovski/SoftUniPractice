using System.Collections.Generic;

namespace Forum.Models
{
    public class Post
    {
        public int Id { get; set; }
        public string PostContent { get; set; }
        public int UserId { get; set; }
        public User User { get; set; }

        public IList<PostAnswer> PostAnswers { get; set; }

    }
}
