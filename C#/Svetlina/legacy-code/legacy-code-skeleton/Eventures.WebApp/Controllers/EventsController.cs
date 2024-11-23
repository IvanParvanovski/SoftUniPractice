using System;
using System.Linq;
using System.Globalization;
using System.Security.Claims;
using System.Collections.Generic;

using Eventures.Data;
using Eventures.WebApp.Models;

using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Authorization;
using Eventures.Services.Contracts;
using AutoMapper;
using Eventures.Services.Models;
using System.Threading.Tasks;
using Eventures.Services.Infrastructure;

namespace Eventures.WebApp.Controllers
{
    [Authorize]
    public class EventsController : Controller
    {
        private readonly IEventService eventService;
        private readonly IMapper mapper;

        public EventsController(IEventService eventService, IMapper mapper)
        {
            this.eventService = eventService;
            this.mapper = mapper;
        }

        [HttpGet]
        public IActionResult All()
        {
            IEnumerable<EventServiceModel> events = this.eventService.GetAllEvents();
            return View(events);
        }

        [HttpGet]
        public IActionResult Create()
        {
            DateTime currentDate = DateTime.Now;
            DateTime startDate = new DateTime(
                currentDate.Year,
                currentDate.Month,
                currentDate.Day,
                currentDate.AddHours(1).Hour,
                currentDate.Minute,
                0);

            DateTime nextDay = DateTime.Now.AddDays(1);
            DateTime endDate = new DateTime(
                nextDay.Year,
                nextDay.Month,
                nextDay.Day,
                currentDate.AddHours(6).Hour,
                currentDate.Minute,
                0);

            EventBindingModel model = new EventBindingModel
            {
                Name = "New Event",
                Place = "Some Place",
                Start = startDate,
                End = endDate,
                PricePerTicket = 10.00M,
                TotalTickets = 100,
                Description = "Lorem Ipsum"
            };

            return View(model);
        }

        [HttpPost]
        public async Task<IActionResult> Create(EventBindingModel bindingModel)
        {
            if (!this.ModelState.IsValid)
            {
                return View(bindingModel);
            }

            string currentUserId = GetUserId();

            await this.eventService.SaveEvent(bindingModel.Name,
                bindingModel.Place,
                bindingModel.Start,
                bindingModel.End,
                bindingModel.TotalTickets,
                bindingModel.PricePerTicket,
                currentUserId,
                bindingModel.Description
                );

            return RedirectToAction(nameof(All));
        }

        [HttpGet]
        public async Task<IActionResult> Delete(int id)
        {
            if (!await this.eventService.EventExists(id))
            {
                return BadRequest();
            }

            if (!await this.eventService.UserOwnsEvent(id, GetUserId()))
            {
                return Unauthorized();
            }

            EventServiceModel serviceModel = await this.eventService.GetEventById(id);
            EventViewModel viewModel = this.mapper.Map<EventViewModel>(serviceModel);
            return View(viewModel);
        }

        [HttpPost]
        public async Task<IActionResult> Delete(EventViewModel eventModel)
        {
            if (!await this.eventService.EventExists(eventModel.Id))
            {
                return BadRequest();
            }

            if (!await this.eventService.UserOwnsEvent(eventModel.Id, GetUserId()))
            {
                return Unauthorized();
            }

            await this.eventService.DeleteEvent(eventModel.Id);
            return RedirectToAction(nameof(All));
        }

        [HttpGet]
        public async Task<IActionResult> Edit(int id)
        {
            if (!await this.eventService.EventExists(id))
            {
                return BadRequest();
            }

            if (!await this.eventService.UserOwnsEvent(id, GetUserId()))
            {
                return Unauthorized();
            }

            EventServiceModel serviceModel = await this.eventService.GetEventById(id);
            EventBindingModel bindingModel = this.mapper.Map<EventBindingModel>(serviceModel);
            return View(bindingModel);
        }

        [HttpPost]
        public async Task<IActionResult> Edit(int id, EventBindingModel bindingModel)
        {
            if (!await this.eventService.EventExists(id))
            {
                return BadRequest();
            }

            if (!await this.eventService.UserOwnsEvent(id, GetUserId()))
            {
                return Unauthorized();
            }

            if (!this.ModelState.IsValid)
            {
                return View(bindingModel);
            }

            await this.eventService.EditEvent(id,
                bindingModel.Name,
                bindingModel.Place,
                bindingModel.Start,
                bindingModel.End,
                bindingModel.TotalTickets,
                bindingModel.PricePerTicket,
                bindingModel.Description);

            return RedirectToAction(nameof(All));
        }

        private string GetUserId()
        {
            return this.User.FindFirstValue(ClaimTypes.NameIdentifier);
        }
    }

}
