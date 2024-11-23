using System.Linq;
using System.Security.Claims;

using Eventures.Data;
using Eventures.Services.Contracts;
using Eventures.WebApp.Models;

using Microsoft.AspNetCore.Mvc;

namespace Eventures.WebApp.Controllers
{
    public class HomeController : Controller
    {
        private readonly IEventService eventService;

        public HomeController(IEventService eventService)
        {
            this.eventService = eventService;
        }

        public IActionResult Index()
        {
            int userEventsCount = -1;

            if (this.User.Identity.IsAuthenticated)
            {
                var currentUserId = User.FindFirst(ClaimTypes.NameIdentifier).Value;
                userEventsCount = this.eventService.GetOwnerEventsCount(currentUserId);
            }

            HomeViewModel homeModel = new HomeViewModel
            {
                AllEventsCount = this.eventService.GetEventsCount(),
                UserEventsCount = userEventsCount
            };

            return View(homeModel);
        }

        public IActionResult Error()
            => View();

        public IActionResult Error401()
            => View();

        public IActionResult Error404()
            => View();
    }
}
