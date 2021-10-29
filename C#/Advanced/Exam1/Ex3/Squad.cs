using System.Collections.Generic;
using System.Linq;

namespace Ex3
{
    public class Squad
    {
        public List<string> players = new List<string>();
        public string Name { get; set; }

        public Squad(string name)
        {
            this.Name = name;
        }

        public void AddPlayer(string name)
        {
            players.Add(name);
        }

        public override string ToString()
        {
            List<string> sortedPlayers = new List<string>();
           
            for (int i = 1; i < this.players.Count; i++)
            {
               sortedPlayers.Add(this.players[i]); 
            }

            sortedPlayers = sortedPlayers.OrderBy(x => x).ToList();
            
            List<string> result = new List<string>
            {
                {this.Name},
                {$"* {this.players[0]}"}
            };
            
            for (int i = 0; i < sortedPlayers.Count(); i++)
            {
                string currentPlayer = sortedPlayers[i];
                string message;
                message = $"** {currentPlayer}";
                
                result.Add(message);
            }
            
            return string.Join("\n", result);
        }
    }
}