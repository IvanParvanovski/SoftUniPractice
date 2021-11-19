namespace ImplementingDoubledLinkedList
{
    public class Node
    {
        public object Element;
        public Node Next;
        public Node Previous;

        public Node(object element)
        {
            this.Element = element;
        }
    }
}