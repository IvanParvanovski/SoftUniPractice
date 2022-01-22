using System;

public class CircularQueue
{
    public int Count { get; private set; }
    private const int InitialCapacity = 16;
    private int[] _elements;
    
    public CircularQueue(int capacity= InitialCapacity)
    {
        _elements = new int[capacity];
    }

    public void Enqueue(int element)
    {
        if (Count == _elements.Length)
        {
            Resize();
        }

        _elements[++Count % _elements.Length] = element;
    }

    public int Dequeue()
    {
        if (Count == 0)
        {
            throw new InvalidOperationException("Queue is empty");
        }

        var element = _elements[0];
        Shift();
        return element;
    }

    public int[] ToArray()
    {
        int[] result = new int[Count];
        Array.Copy(_elements, result, Count);
        return result;
    }
    
    private void Resize()
    {
        int[] newArray = new int[_elements.Length * 2];
        Array.Copy(_elements, newArray, _elements.Length);
        _elements = newArray;
    }
    
    private void Shift()
    {
        for (var i = 0; i < Count - 1; i++)
        {
            _elements[i] = _elements[i + 1];
        }

        Count--;
    }
}


class Example
{
    static void Main()
    {
        var queue = new CircularQueue();

        queue.Enqueue(1);
        queue.Enqueue(2);
        queue.Enqueue(3);
        queue.Enqueue(4);
        queue.Enqueue(5);
        queue.Enqueue(6);

        Console.WriteLine("Count = {0}", queue.Count);
        Console.WriteLine(string.Join(", ", queue.ToArray()));
        Console.WriteLine("---------------------------");

        var first = queue.Dequeue();
        Console.WriteLine("First = {0}", first);
        Console.WriteLine("Count = {0}", queue.Count);
        Console.WriteLine(string.Join(", ", queue.ToArray()));
        Console.WriteLine("---------------------------");

        queue.Enqueue(-7);
        queue.Enqueue(-8);
        queue.Enqueue(-9);
        Console.WriteLine("Count = {0}", queue.Count);
        Console.WriteLine(string.Join(", ", queue.ToArray()));
        Console.WriteLine("---------------------------");

        first = queue.Dequeue();
        Console.WriteLine("First = {0}", first);
        Console.WriteLine("Count = {0}", queue.Count);
        Console.WriteLine(string.Join(", ", queue.ToArray()));
        Console.WriteLine("---------------------------");

        queue.Enqueue(-10);
        Console.WriteLine("Count = {0}", queue.Count);
        Console.WriteLine(string.Join(", ", queue.ToArray()));
        Console.WriteLine("---------------------------");

        first = queue.Dequeue();
        Console.WriteLine("First = {0}", first);
        Console.WriteLine("Count = {0}", queue.Count);
        Console.WriteLine(string.Join(", ", queue.ToArray()));
        Console.WriteLine("---------------------------");
    }
}
