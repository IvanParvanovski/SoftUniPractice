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
            int expectedGuestEventCount = this.dbContext.Events.Count(e => e.OwnerId == this.testDb.GuestUser.Id);
            Assert.AreEqual(expectedGuestEventCount, guestEventCount);

            int userMariaEventCount = this.eventService.GetOwnerEventsCount(this.testDb.UserMaria.Id);
            int expectedMariaEventCount = this.dbContext.Events.Count(e => e.OwnerId == this.testDb.UserMaria.Id);
            Assert.AreEqual(expectedMariaEventCount, userMariaEventCount);
        }

        [Test]
        public void Test_GetEventsCount_ReturnsCorrectCount()
        {
            int dbEventCount = this.eventService.GetEventsCount();
            int expectedEventsCount = this.dbContext.Events.Count();

            Assert.AreEqual(expectedEventsCount, dbEventCount);
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
            int expectedId = this.testDb.EventOpenFest.Id;

            bool dbResult = await this.eventService.EventExists(expectedId);

            Assert.IsTrue(dbResult);
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

            string mariaId = this.testDb.UserMaria.Id;
            validResult = await this.eventService.UserOwnsEvent(eventGuest, mariaId);
            Assert.IsFalse(validResult);

            int eventId = 10;
            Assert.False(await this.eventService.UserOwnsEvent(eventId, mariaId));
            //string mariaId = this.testDb.UserMaria.Id;
            //bool res = await this.eventService.UserOwnsEvent(this.testDb.EventDevConf.Id, mariaId);
            //Assert.True(res);
        }

        [Test]
        public async Task Test_GetEventById_ReturnsCorrectResultAsync()
        {

            Event expectedResult = this.testDb.EventDevConf;
            EventServiceModel actualModel = await this.eventService.GetEventById(expectedResult.Id);

            Assert.AreEqual(expectedResult.Id, actualModel.Id);
            Assert.AreEqual(expectedResult.Name, actualModel.Name);
            Assert.AreEqual(expectedResult.Owner.UserName, actualModel.Owner);
            Assert.AreEqual(expectedResult.PricePerTicket, actualModel.PricePerTicket);
            Assert.AreEqual(expectedResult.TotalTickets, actualModel.TotalTickets);
            Assert.AreEqual(expectedResult.Description, actualModel.Description);
            Assert.AreEqual(expectedResult.Place, actualModel.Place);
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
            string newEventName = "TestEventName";
            string newEventPlace = "TestEventPlace";
            DateTime newEventStart = new DateTime();
            DateTime newEventEnd = new DateTime();
            int newEventTotalTickets = 1;
            decimal newEventPricePerTicket = (decimal)1.11;
            string newEventOwnerId = testDb.GuestUser.Id;
            string newEventDescription = "TestEventDescription";

            await this.eventService.SaveEvent(newEventName, newEventPlace, newEventStart, newEventEnd, newEventTotalTickets, newEventPricePerTicket, newEventOwnerId,newEventDescription);

            Event ev = this.dbContext.Events.Include(e => e.Owner).LastOrDefault();

            Assert.AreEqual(newEventName, ev.Name);
            Assert.AreEqual(newEventPlace, ev.Place);
            Assert.AreEqual(newEventStart, ev.Start);
            Assert.AreEqual(newEventEnd, ev.End);
            Assert.AreEqual(newEventTotalTickets, ev.TotalTickets);
            Assert.AreEqual(newEventPricePerTicket, ev.PricePerTicket);
            Assert.AreEqual(newEventOwnerId, ev.OwnerId);
            Assert.AreEqual(newEventDescription, ev.Description);
        }

        [Test]
        public async Task Test_DeleteEvent_RemovesCorrectlyAsync()
        {
            string newEventName = "TestEventName";
            string newEventPlace = "TestEventPlace";
            DateTime newEventStart = new DateTime();
            DateTime newEventEnd = new DateTime();
            int newEventTotalTickets = 1;
            decimal newEventPricePerTicket = (decimal)1.11;
            string newEventOwnerId = testDb.GuestUser.Id;
            string newEventDescription = "TestEventDescription";

            await this.eventService.SaveEvent(newEventName, newEventPlace, newEventStart, newEventEnd, newEventTotalTickets, newEventPricePerTicket, newEventOwnerId, newEventDescription);

            Event ev = this.dbContext.Events.LastOrDefault();

            await this.eventService.DeleteEvent(ev.Id);

            Assert.IsNull(this.dbContext.Events.FirstOrDefault(e => e.Id == ev.Id));
        }

        [Test]
        public async Task Test_EditEvent_ChangesCorrectlyAsync()
        {
            string newEventName = "TestEventName";
            string newEventPlace = "TestEventPlace";
            DateTime newEventStart = new DateTime();
            DateTime newEventEnd = new DateTime();
            int newEventTotalTickets = 1;
            decimal newEventPricePerTicket = (decimal)1.11;
            string newEventOwnerId = testDb.GuestUser.Id;
            string newEventDescription = "TestEventDescription";

            await this.eventService.SaveEvent(newEventName, newEventPlace, newEventStart, newEventEnd, newEventTotalTickets, newEventPricePerTicket, newEventOwnerId, newEventDescription);

            int eventId = this.dbContext.Events.LastOrDefault()!.Id;

            decimal newPrice = 2.0m;

            await this.eventService.EditEvent(eventId, newEventName, newEventPlace, newEventStart, newEventEnd, newEventTotalTickets, newPrice, newEventDescription);

            Event ev = this.dbContext.Events.LastOrDefault();

            Assert.AreEqual(eventId, ev.Id);
            Assert.AreEqual(newPrice, ev.PricePerTicket);
        }
    }
}
