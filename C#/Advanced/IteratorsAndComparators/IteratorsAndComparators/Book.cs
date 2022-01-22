using System;
using System.Collections.Generic;

namespace IteratorsAndComparators
{
    public class Book : 
        IComparable<Book>
    {
        public Book(string title, int year, params string[] authors)
        {
            this.Title = title;
            this.Year = year;
            this.Authors = new List<string>(authors);
        }
        
        public string Title { get; set; }
        public int Year { get; set; }
        public List<string> Authors { get; set; }
        
        // public int CompareTo(Book other)
        // {
        //     int result = this.Year.CompareTo(other.Year);
        //
        //     if (result == 0)
        //     {
        //         result = this.Title.CompareTo(other.Title);
        //     }
        //
        //     return result;
        // }

        public override string ToString()
        {
            return $"{this.Title} - ${this.Year}";
        }

        public int CompareTo(Book x)
        {
            
            int result = this.Year.CompareTo(x.Year);
            // 1000 2015 2020 2021 2021
            // 2020 -> Titan
            // 2020 -> Financier
            // Financier
        
            // > 0 (размяна)
            // < 0 (остава непроменено)
            // == 0 (еднакви)
            
            if (result == 0)
            {
                result = this.Title.CompareTo(x.Title);
            }
        
            return result;
        }
    }
}