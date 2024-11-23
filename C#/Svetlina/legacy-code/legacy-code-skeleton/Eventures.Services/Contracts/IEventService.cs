using System;
using Eventures.Services.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Eventures.Services.Contracts
{
	public interface IEventService
	{
        int GetOwnerEventsCount(string ownerId);

        int GetEventsCount();

        IEnumerable<EventServiceModel> GetAllEvents();

        Task<bool> EventExists(int id);

        Task<bool> UserOwnsEvent(int eventId, string userId);

        Task<EventServiceModel> GetEventById(int id);

        Task SaveEvent(string name, string place,
            DateTime start, DateTime end, int totalTickets,
            decimal pricePerTicket, string ownerId, string description);

        Task DeleteEvent(int id);

        Task EditEvent(int id, string name, string place,
            DateTime start, DateTime end, int totalTickets, decimal pricePerTicket, string description);
    }
}

