using System;
using System.Collections.Generic;
using System.Linq;

class DijkstraAlgorithm
{
    static void Main()
    {
        // Example graph represented as an adjacency list
        Dictionary<string, Dictionary<string, int>> graph = new Dictionary<string, Dictionary<string, int>>
        {
            { "A", new Dictionary<string, int> { { "B", 1 }, { "C", 4 } } },
            { "B", new Dictionary<string, int> { { "A", 1 }, { "C", 2 }, { "D", 5 } } },
            { "C", new Dictionary<string, int> { { "A", 4 }, { "B", 2 }, { "D", 1 } } },
            { "D", new Dictionary<string, int> { { "B", 5 }, { "C", 1 } } }
        };

        string startVertex = "A";
        Dictionary<string, int> shortestDistances = Dijkstra(graph, startVertex);

        // Display the shortest distances from the start vertex to each vertex
        Console.WriteLine("Shortest Distances from " + startVertex + ":");
        foreach (var vertex in shortestDistances)
        {
            Console.WriteLine($"{vertex.Key}: {vertex.Value}");
        }
    }

    static Dictionary<string, int> Dijkstra(Dictionary<string, Dictionary<string, int>> graph, string startVertex)
    {
        var shortestDistances = new Dictionary<string, int>();
        var priorityQueue = new PriorityQueue<string>();

        // Initialize distances with infinity, except for the start vertex
        foreach (var vertex in graph.Keys)
        {
            shortestDistances[vertex] = int.MaxValue;
            priorityQueue.Enqueue(vertex, int.MaxValue);
        }
        shortestDistances[startVertex] = 0;
        priorityQueue.Enqueue(startVertex, 0);

        while (priorityQueue.Count > 0)
        {
            var currentVertex = priorityQueue.Dequeue();

            foreach (var neighbor in graph[currentVertex])
            {
                int newDistance = shortestDistances[currentVertex] + neighbor.Value;

                if (newDistance < shortestDistances[neighbor.Key])
                {
                    shortestDistances[neighbor.Key] = newDistance;
                    priorityQueue.Enqueue(neighbor.Key, newDistance);
                }
            }
        }

        return shortestDistances;
    }
}

class PriorityQueue<T>
{
    private List<(T, int)> elements;

    public PriorityQueue()
    {
        elements = new List<(T, int)>();
    }

    public int Count
    {
        get { return elements.Count; }
    }

    public void Enqueue(T item, int priority)
    {
        elements.Add((item, priority));
        elements = elements.OrderBy(e => e.Item2).ToList();
    }

    public T Dequeue()
    {
        var item = elements.First().Item1;
        elements.RemoveAt(0);
        return item;
    }
}