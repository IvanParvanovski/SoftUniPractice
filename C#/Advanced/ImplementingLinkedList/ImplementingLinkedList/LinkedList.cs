using System;
using ImplementingLinkedList;

namespace ImplementLinkedList
{
    public class LinkedList
    {
        private Node head;
        private Node tail;
        private int count;
        
        public LinkedList()
        {
            head = null;
            tail = null;
            count = 0;
        }
        
        public void Add(object data)
        {
            Node node = new Node(data);
            if (head == null)
            {
                head = node;
                tail = node;
            }
            else
            {
                tail.Next = node;
                tail = node;
            }
            count++;
        }

        public void Remove(object data)
        {
            Node current = head;
            Node previous = null;
            
            while (current != null)
            {
                if (current.Element.Equals(data))
                {
                    if (previous == null)
                    {
                        head = current.Next;
                    }
                    else
                    {
                        previous.Next = current.Next;
                    }
                    count--;
                    return;
                }
                previous = current;
                current = current.Next;
            }
        }
        
        public void RemoveAt(int index)
        {
            if (index < 0 || index >= count)
            {
                throw new IndexOutOfRangeException();
            }
            Node current = head;
            Node previous = null;
            int i = 0;
            while (i < index)
            {
                previous = current;
                current = current.Next;
                i++;
            }
            if (previous == null)
            {
                head = current.Next;
            }
            else
            {
                previous.Next = current.Next;
            }
            count--;
        }
        
        public void Clear()
        {
            head = null;
            tail = null;
            count = 0;
        }
        
        public int IndexOf(object data)
        {
            Node current = head;
            int i = 0;
            while (current != null)
            {
                if (current.Element.Equals(data))
                {
                    return i;
                }
                current = current.Next;
                i++;
            }
            return -1;
        }
        
        public bool Contains(object data)
        {
            Node current = head;
            while (current != null)
            {
                if (current.Element.Equals(data))
                {
                    return true;
                }
                current = current.Next;
            }
            return false;
        }
        
        public object ElementAt(int index)
        {
            if (index < 0 || index >= count)
            {
                throw new IndexOutOfRangeException();
            }
            Node current = head;
            int i = 0;
            while (i < index)
            {
                current = current.Next;
                i++;
            }
            return current.Element;
        }

        public object this[int index]
        {
            get
            {
                return ElementAt(index);
            }
            set
            {
                if (index < 0 || index >= count)
                {
                    throw new IndexOutOfRangeException();
                }
                Node current = head;
                int i = 0;
                while (i < index)
                {
                    current = current.Next;
                    i++;
                }
                current.Element = value;
            }
        }
        
        public int Count
        {
            get
            {
                return count;
            }
        }
        
    }
}