namespace ImplementingLinkedList
{
    public class Node
    {
        public object Element { get; set; }
        public Node Next { get; set; }

        public Node(object element, Node prevNode)
        {
            this.Element = element;
            prevNode.Next = this;
            Next = null;
        }
        
        public Node(object element)
        {
            this.Element = element;
            Next = null;
        }
    }
}