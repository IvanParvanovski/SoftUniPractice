using System;
using System.Collections.Generic;

namespace Ex5ListyIterator
{
    public class ListyIterator
    {
        private List<object> _elements;
        private int _index;
        
        public ListyIterator(object[] elements)
        {
            this.Elements = new List<object>(elements);
        }

        public bool Move()
        {
            if (HasNext())
            {
                _index++;
                return true;
            }

            return false;
        }

        public void Print()
        {
            if (_elements.Count == 0)
            {
                throw new Exception("Invalid Operation!");
            }
            
            Console.WriteLine(_elements[_index]);
        }

        public bool HasNext()
        {
            return _index < _elements.Count;
        }
        
        public List<object> Elements { get; set; }

    }
}