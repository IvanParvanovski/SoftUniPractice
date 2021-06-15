using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex4SongsQueue
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<string> songs = new Queue<string>(Console.ReadLine()!.Split(", "));
            
            while (songs.Count > 0)
            {
                string[] input = Console.ReadLine()!.Split();
                string command = input[0];
                
                switch (command)
                {
                    case "Play":
                        songs.Dequeue();
                        break;
                    case "Add":
                        string song = string.Join(" ", input.Skip(1)); ;
                        if (!songs.Contains(song))
                        {
                            songs.Enqueue(song);
                        }
                        else
                        {
                            Console.WriteLine($"{song} is already contained!");
                        }
                        break;
                    case "Show":
                        string songsAsString = string.Join(", ", songs);
                        Console.WriteLine(songsAsString);
                        break;
                }
            }

            Console.WriteLine("No more songs!");
        }
    }
}