namespace Revision
{
    public class Program
    {
        public static void Main(string[] args)
        {
            
        }
    }
}


var author = context.Books.Include(book => book.author).Select().Where().OrderBy().ToList();