using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Globalization;
using System.Threading;
using Wintellect.PowerCollections;

namespace DataStructuresExercises
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Thread.CurrentThread.CurrentCulture = CultureInfo.InvariantCulture;
            
            int n = int.Parse(Console.ReadLine());
            var events = new OrderedMultiDictionary<DateTime, string>(true);

            for (int i = 0; i < n; i++)
            {
                string[] eventTokens = Console.ReadLine().Split('|');
                string eventName = eventTokens[0].Trim();
                DateTime eventDate = DateTime.Parse(eventTokens[1].Trim());
                events.Add(eventDate, eventName);
            }

            foreach (var ev in events)
            {
                Console.WriteLine(ev.Value + " | " + ev.Key.ToString("dd-MMM-yyyy hh:mm"));
            }
        }
    }
}