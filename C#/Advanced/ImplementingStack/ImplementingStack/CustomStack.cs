using System;

namespace ImplementingStack
{
    public class CustomStack
    {
        private int[] items;
        private int count;

        public CustomStack()
        {
            
        }

        public int Count
        {
            get => count; 
            set => count = value;
        }

        public void Push(int item)
        {
            if (count >= items.Length)
            {
                Grow();
            }

            items[count] = item;
            count++;
        }

        public int Peek()
        {
            if (count == 0)
            {
                throw new InvalidOperationException("The stack is empty");
            }
            
            int lastItem = items[count - 1];
            return lastItem;
        }

        public int Pop()
        {
            if (count == 0)
            {
                throw new InvalidOperationException("The stack is empty");
            }

            int lastElement = items[count - 1];
            items[count - 1] = 0;
            count--;
            return lastElement;
        }

        public void ForEach(Action<object> action)
        {
            for (int i = 0; i < count; i++)
            {
                action(items[i]);
            }
        }
        private void Grow()
        {
            int[] newArray = new int[items.Length];
            Array.Copy(items, newArray, newArray.Length);
            items = newArray;
        }
    }
}