using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3
{
    class Program
    {
        static void Main(string[] args)
        {
            int teamsCount = int.Parse(Console.ReadLine()!);
            Dictionary<string, Squad> squads = new Dictionary<string, Squad>();
            
            for (int i = 0; i < teamsCount; i++)
            {
                string[] squadTokens = Console.ReadLine()!.Split('-');

                string creator = squadTokens[0];
                string name = squadTokens[1];
                Squad squad = new Squad(name);

                if (squads.Values.Count(x => x.Name == name) != 0)
                {
                    Console.WriteLine("That squad name is already taken.");
                }
                else if (squads.ContainsKey(creator))
                {
                    Console.WriteLine($"{creator} cannot set up another squad.");
                }
                else
                {
                    squad.AddPlayer(creator);
                    squads[creator] = squad;
                    Console.WriteLine($"{creator} has successfully created a new squad: {name}");
                }
            }

            while (true)
            {
                string teamInfo = Console.ReadLine()!;

                if (teamInfo == "end")
                {
                    break;
                }
                
                string[] squadTokens = teamInfo!.Split("/");
                
                string playerName = squadTokens[0];
                string squadName = squadTokens[1];

                if (squads.Values.Count(x => x.Name == squadName) == 0)
                {
                    Console.WriteLine("The squad doesn't exist.");
                    continue;
                } 
                
                if (squads.Values.Count(x => x.players.Contains(playerName)) != 0)
                {
                    Console.WriteLine("The player is already member of a squad.");    
                    continue;
                }

                foreach (KeyValuePair<string, Squad> squad in squads)
                {
                    if (squad.Value.Name == squadName)
                    {
                        squad.Value.AddPlayer(playerName);
                        break;
                    }
                }
            }

            List<string> detached = new List<string>();
            foreach (Squad squad in squads.Values.OrderByDescending(s => s.players.Count()).ThenBy(s => s.Name))
            {
                if (squad.players.Count() > 1)
                {
                    Console.WriteLine(squad.ToString());
                }
                else
                {
                    detached.Add(squad.Name);
                }
            }

            Console.WriteLine("Squads to detach:");
            foreach (string squadName in detached)
            {
                Console.WriteLine(squadName);
            }
        }
    }
}