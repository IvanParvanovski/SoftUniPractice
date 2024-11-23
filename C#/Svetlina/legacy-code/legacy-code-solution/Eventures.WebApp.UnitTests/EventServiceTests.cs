using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Eventures.Data;
using Eventures.Services;
using Eventures.Services.Contracts;
using Eventures.Services.Models;

using Microsoft.EntityFrameworkCore;

using NUnit.Framework;

namespace Eventures.WebApp.UnitTests
{
    [TestFixture]
    public class EventServiceTests : UnitTestsBase
    {
        private IEventService eventService;

        [SetUp]
        public void SetUp()
        {
            this.eventService = new EventService(this.dbContext, this.mapper);
        }

        [Test]
        public void Test_GetOwnerEventsCount_ReturnsCorrectCount()
        {
            int guestEventCount = this.eventService.GetOwnerEventsCount(this.testDb.GuestUser.Id);
            int expectedGuestEventCount = this.dbContext.Events
                .Count(e => e.OwnerId == this.testDb.GuestUser.Id);
            Assert.AreEqual(expectedGuestEventCount, guestEventCount);

            int userMariaEventCount = this.eventService.GetOwnerEventsCount(this.testDb.UserMaria.Id);
            int expectedMariaEventCount = this.dbContext.Events
                .Count(e => e.OwnerId == this.testDb.UserMaria.Id);
            Assert.AreEqual(expectedMariaEventCount, userMariaEventCount);
        }

        [Test]
        public void Test_GetEventsCount_ReturnsCorrectCount()
        {
            int dbEventCount = this.eventService.GetEventsCount();
            int expectedEventCount = this.dbContext.Events.Count();

            Assert.AreEqual(expectedEventCount, dbEventCount);
        }

        [Test]
        public void Test_GetAllEvents_ReturnsCorrectEvents()
        {
            List<EventServiceModel> dbEvents = this.eventService.GetAllEvents().ToList();
            List<Event> expectedEvents = this.dbContext.Events.ToList();

            Assert.AreEqual(expectedEvents.Count, dbEvents.Count);
            
            for (int i = 0; i < dbEvents.Count; i++)
            {
                Assert.AreEqual(expectedEvents[i].Name, dbEvents[i].Name);
            }
        }

        [Test]
        public async Task Test_EventExists_ReturnsCorrectValueAsync()
        {
            int existingId = this.testDb.EventOpenFest.Id;
            bool validResult = await this.eventService.EventExists(existingId);

            Assert.IsTrue(validResult);
        }

        [Test]
        public async Task Test_EventExists_ReturnsCorrectValue_InvalidIdAsync()
        {
            int nonExistingId = 10;
            bool invalidResult = await this.eventService.EventExists(nonExistingId);

            Assert.IsFalse(invalidResult);
        }

        [Test]
        public async Task Test_UserOwnsEvent_ReturnsCorrectValueAsync()
        {
            int eventGuest = this.testDb.EventOpenFest.Id;
            string guestId = this.testDb.GuestUser.Id;
            bool validResult = await this.eventService.UserOwnsEvent(eventGuest, guestId);
            Assert.IsTrue(validResult);

            string mariaId = this.testDb.UserMaria.Id;
            validResult = await this.eventService.UserOwnsEvent(eventGuest, mariaId);
            Assert.IsFalse(validResult);

            int eventId = 10;
            Assert.IsFalse(await this.eventService.UserOwnsEvent(eventId, mariaId));
        }

        [Test]
        public async Task Test_GetEventById_ReturnsCorrectResultAsync()
        {
            Event ev = this.testDb.EventDevConf;
            EventServiceModel actualModel = await this.eventService.GetEventById(ev.Id);

            Assert.AreEqual(ev.Id, actualModel.Id);
            Assert.AreEqual(ev.Name, actualModel.Name);
            Assert.AreEqual(ev.Place, actualModel.Place);
            Assert.AreEqual(ev.TotalTickets, actualModel.TotalTickets);
            Assert.AreEqual(ev.PricePerTicket, actualModel.PricePerTicket);
            Assert.AreEqual(ev.Owner.UserName, actualModel.Owner);
            Assert.AreEqual(ev.Description, actualModel.Description);
        }

        [Test]
        public async Task Test_GetEventById_ReturnsCorrectResult_InvalidIdAsync()
        {
            int invalidId = 10;
            Assert.IsNull(await this.eventService.GetEventById(invalidId));
        }

        [Test]
        public async Task Test_SaveEvent_AddsCorrectlyAsync()
        {
            string name = "TestEvent";
            string place = "TestPlace";
            DateTime start = new DateTime(2015, 12, 28);
            DateTime end = new DateTime(2015, 12, 31);
            int totalTickets = 200;
            decimal pricePerTicket = 1.0m;
            string ownerId = this.testDb.GuestUser.Id;
            string description = "Lorem ipsum";

            await this.eventService.SaveEvent(name, place, start, end, totalTickets, pricePerTicket, ownerId,
                description);

            Event ev = this.dbContext.Events
                .Include(e => e.Owner)
                .LastOrDefault();

            Assert.AreEqual(name, ev.Name);
            Assert.AreEqual(start, ev.Start);
            Assert.AreEqual(end, ev.End);
            Assert.AreEqual(place, ev.Place);
            Assert.AreEqual(totalTickets, ev.TotalTickets);
            Assert.AreEqual(pricePerTicket, ev.PricePerTicket);
            Assert.AreEqual(ownerId, ev.Owner.Id);
            Assert.AreEqual(description, ev.Description);
        }

        [Test]
        public async Task Test_DeleteEvent_RemovesCorrectlyAsync()
        {
            string name = "TestEvent";
            string place = "TestPlace";
            DateTime start = new DateTime(2015, 12, 28);
            DateTime end = new DateTime(2015, 12, 31);
            int totalTickets = 200;
            decimal pricePerTicket = 1.0m;
            string ownerId = this.testDb.GuestUser.Id;
            string description = "Lorem ipsum";

            await this.eventService.SaveEvent(name, place, start, end, totalTickets, pricePerTicket, ownerId,
                description);

            Event ev = this.dbContext.Events
                .LastOrDefault();

            await this.eventService.DeleteEvent(ev.Id);

            Assert.IsNull(this.dbContext.Events.FirstOrDefault(e => e.Id == ev.Id));
        }

        [Test]
        public async Task Test_EditEvent_ChangesCorrectlyAsync()
        {
            string name = "TestEvent";
            string place = "TestPlace";
            DateTime start = new DateTime(2015, 12, 28);
            DateTime end = new DateTime(2015, 12, 31);
            int totalTickets = 200;
            decimal pricePerTicket = 1.0m;
            string ownerId = this.testDb.GuestUser.Id;
            string description = "Lorem ipsum";

            await this.eventService.SaveEvent(name, place, start, end, totalTickets, pricePerTicket, ownerId,
                description);

            int eventId = this.dbContext.Events
                .LastOrDefault()!.Id;

            decimal newPrice = 2.0m;

            await this.eventService.EditEvent(eventId, name, place, start, end, totalTickets, newPrice, description);
            
            Event ev = this.dbContext.Events
                .LastOrDefault();
            Assert.AreEqual(eventId, ev.Id);
            Assert.AreEqual(newPrice, ev.PricePerTicket);
        }
    }
}
