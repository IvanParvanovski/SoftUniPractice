using System;

namespace ImplementingArrayList
{
    public class CustomArrayList
    {
        private object[] arr;
        private int count;
        public int Count
        {
            get { return count; }
            private set { count = value; }
        }
        private static readonly int INITIAL_CAPACITY = 4;
        
        public CustomArrayList()
        {
            arr = new object[INITIAL_CAPACITY];
            count = 0;
        }
        
        public void Add(object item)
        {
            Insert(count, item);
            this.count++;
        }
        
        public void Insert(int index, object item)
        {
            this.count += 1;
        }
        
        public int IndexOf(object item)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] == item)
                {
                    return i;
                }
            }

            return -1;
        }
        
        public void Clear()
        {
            this.count = 0;
            this.arr = new object[0];
        }
        
        public bool Contains(object item)
        {
            foreach (object i in arr)
            {
                if (i == item)
                {
                    return true;
                }
            }

            return false;
        }

        public object this[int index]
        {
            get
            {
                if (index < 0 || index > this.arr.Length)
                {
                    throw new IndexOutOfRangeException("Index out of range!");
                }
                
                return this.arr[index];
            }
            set
            {
                if (index < 0 || index > this.arr.Length)
                {
                    throw new IndexOutOfRangeException("Index out of range!");
                }
                
                this.arr[index] = value;
            }
        }

        // public object Remove(int index)
        // {
        //     this.count -= 1;
        // }
        // public int Remove(object item)
        // {
        //     this.count -= 1;
        // }
        
        public void Resize()
        {
            
        }

        public void Shrink()
        {
            
        }
    }
}