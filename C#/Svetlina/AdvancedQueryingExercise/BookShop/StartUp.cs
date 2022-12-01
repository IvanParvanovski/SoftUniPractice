using System.Linq;

namespace BookShop
{
    using Data;
    using Initializer;

    public class StartUp
    {
        public static void Main()
        {
            using var db = new BookShopContext();
            DbInitializer.ResetDatabase(db);

            GetBooksByAgeRestriction(db, );
        }

        public static string GetBooksByAgeRestriction(
            BookShopContext context, 
            string command)
        {
            var books = context.Books
                .Where(b => b.AgeRestriction.Equals(command))
                .Select(b => new(Title = b.Title));

            return books.ToString();
        }
    }
}
