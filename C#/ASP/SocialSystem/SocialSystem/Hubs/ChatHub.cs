using System.Threading.Tasks;
using Microsoft.AspNetCore.SignalR;

namespace SocialSystem.Models.Hubs
{
    public class ChatHub : Hub
    {
        public async Task SendMessage(Message message) => 
            await Clients.All.SendAsync("receiveMessage", message);
    }
}