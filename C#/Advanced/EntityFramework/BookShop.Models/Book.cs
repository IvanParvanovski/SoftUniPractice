//using BookShop.Models.Enums;

namespace BookShop.Models
{
    using System;
    using System.Collections.Generic;

    public class Book
    {
        public Book()
        {

        }

        public int BookId { get; set; }

        public string Title { get; set; }

        public string Description { get; set; }

        public decimal Price { get; set; }

        public int AuthorId { get; set; }
        public Author Author { get; set; }

    }
}
