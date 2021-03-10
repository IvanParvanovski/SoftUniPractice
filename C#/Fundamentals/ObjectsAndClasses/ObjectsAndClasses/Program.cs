using System;
using System.Collections.Generic;

namespace ObjectsAndClasses
{
    public class Song
    {
        public string TypeList { get; set; }
        public string Name { get; set; }
        public string Time { get; set; }
    
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            int soungsCount = int.Parse(Console.ReadLine());
            Song[] songs = new Song[soungsCount];

            for (int i = 0; i < soungsCount; i++)
            {
                string[] songData = Console.ReadLine().Split('_', StringSplitOptions.RemoveEmptyEntries);
                string typeList = songData[0];
                string name = songData[1];
                string time = songData[2];
                Song song = new Song { TypeList = typeList, Name = name, Time = time };
                songs[i] = song;
            }

            string type = Console.ReadLine();

            foreach (Song song in songs)
                if (song.TypeList == type || type == "all")
                    Console.WriteLine($"{song.Name}");
        }
    }
}
