using Forum.Data;


namespace Forum
{
    public class StartUp
    {
        static void Main(string[] args)
        {
            var context = new ForumDbContext();

        }
        public static string ImportUsers(ForumDbContext context, string inputXml)
        {
            //TODO...
            return $"";
        }

        public static string ImportPosts(ForumDbContext context, string inputXml)
        {
            //TODO...
            return $"";
        }

        public static string ImportPostsAnswers(ForumDbContext context, string inputXml)
        {
            //TODO...
            return $"";
        }

        public static string GetPostsWithPostAnswers(ForumDbContext context)
        {
            //TODO...
            return "";
        }

    }
}
