using System;
using System.Linq;

namespace IteratorsAndComparators
{
    class Program
    {
        static void Main(string[] args)
        {
            // Book bookOne = new Book("Animal Farm", 2003, "George Orwell");
            // Book bookTwo = new Book("The Documents in the Case", 2002,
            //     "Dorothy Sayers", "Robert Eustace");
            // Book bookThree = new Book("The Documents in the Case", 1930);
            // BookComparator bookComparator = new BookComparator();
            // OrderBy(x => x, bookComparator)


            Book firstBook = new Book("Gosho", 2008, "A", "B");
            Book secondBook = new Book("Pesho", 2005, "C", "D");
            Book thirdBook = new Book("Ivan", 2010, "E", "F");
            
            // Gosho, Pesho, Ivan
            // Gosho Pesho
            
            Library libraryTwo = new Library(firstBook, secondBook, thirdBook);
            
            
            foreach (var book in libraryTwo.OrderBy(x => x))
            {
                Console.WriteLine(book.Title);
            }
        }
    }
}
