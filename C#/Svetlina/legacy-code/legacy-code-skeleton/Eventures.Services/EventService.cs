using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using AutoMapper;
using Eventures.Data;
using Eventures.Services.Contracts;
using Eventures.Services.Models;
using Microsoft.EntityFrameworkCore;

namespace Eventures.Services
{
    public class EventService : IEventService
    {
        private readonly ApplicationDbContext context;
        private readonly IMapper mapper;

        public EventService(ApplicationDbContext context, IMapper mapper)
        {
            this.context = context;
            this.mapper = mapper;
        }

        public int GetOwnerEventsCount(string ownerId)
        {
            return this.context.Events.Count(e => e.OwnerId == ownerId);
        }

        public int GetEventsCount()
        {
            return this.context.Events.Count();
        }

        public IEnumerable<EventServiceModel> GetAllEvents()
        {
            List<EventServiceModel> events = this.mapper.Map<List<EventServiceModel>>(
                this.context.Events.Include(e => e.Owner).ToList());

            return events;
        }

        public async Task<bool> EventExists(int id)
        {
            return await this.context.Events.FindAsync(id) != null;
        }

        public async Task<bool> UserOwnsEvent(int eventId, string userId)
        {
            Event ev = await this.context.Events.FindAsync(eventId);

            if (ev == null)
            {
                return false;
            }

            return ev.OwnerId == userId;
        }

        public async Task<EventServiceModel> GetEventById(int id)
        {
            Event ev = await this.context.Events
                .Include(e => e.Owner)
                .FirstOrDefaultAsync(e => e.Id == id);

            return ev == null ? null : this.mapper.Map<EventServiceModel>(ev);

        }

        public async Task SaveEvent(
            string name,
            string place,
            DateTime start,
            DateTime end,
            int totalTickets,
            decimal pricePerTicket,
            string ownerId,
            string description)
        {
            Event eventForDb = new Event
            {
                Name = name,
                Place = place,
                Start = start,
                End = end,
                TotalTickets = totalTickets,
                PricePerTicket = pricePerTicket,
                OwnerId = ownerId,
                Description = description
            };

            await this.context.Events.AddAsync(eventForDb);
            await this.context.SaveChangesAsync();
        }

        public async Task DeleteEvent(int id)
        {
            Event ev = await this.context.Events.FindAsync(id);
            this.context.Events.Remove(ev);
            await this.context.SaveChangesAsync();
        }

        public async Task EditEvent(
            int id,
            string name,
            string place,
            DateTime start,
            DateTime end,
            int totalTickets,
            decimal pricePerTicket,
            string description)
        {
            Event ev = await this.context.Events.FindAsync(id);

            ev.Name = name;
            ev.Place = place;
            ev.Start = start;
            ev.End = end;
            ev.TotalTickets = totalTickets;
            ev.PricePerTicket = pricePerTicket;
            ev.Description = description;

            await this.context.SaveChangesAsync();
        }
    }
}

