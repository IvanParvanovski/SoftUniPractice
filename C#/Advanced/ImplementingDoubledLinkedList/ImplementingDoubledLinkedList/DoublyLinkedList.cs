using System;

namespace ImplementingDoubledLinkedList
{
    public class DoublyLinkedList
    {
        private Node head;
        private Node tail;
        
        private int Count { get; set; }

        public void AddFirst(object element)
        {
            Node node = new Node(element);

            if (Count == 0)
            {
                head = tail = node;
                Count++;

                return;
            }
            
            head.Previous = node;
            node.Next = head;
            head = node;
            Count++;
        }

        public void AddLast(object element)
        {
            Node node = new Node(element);
            
            if (Count == 0)
            {
                head = tail = node;
                Count++;
            
                return;
            }
            
            tail.Next = node;
            node.Previous = tail;
            tail = node;
            Count++;
        }

        public void RemoveFirst()
        {
            IsEmpty();
            head = head.Next;
            head.Previous = null;
            Count--;
        }

        public void RemoveLast()
        {
            IsEmpty();
            if (Count == 1)
            {
                tail = head = null;
                Count--;
                return;
            }
            
            tail = tail.Previous;
            tail.Next = null;
            Count--;
        }

        public object GetFirst()
        {
            IsEmpty();
            return head.Element;
        }

        public object GetLast()
        {
            IsEmpty();
            return tail.Element;
        }

        public void IsEmpty()
        {
            if (Count == 0)
            {
                throw new InvalidOperationException("Linked List is empty!");
            }
        }
    }
}