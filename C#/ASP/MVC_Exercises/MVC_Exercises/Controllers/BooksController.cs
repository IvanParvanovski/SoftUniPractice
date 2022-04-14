using Microsoft.AspNetCore.Mvc;

namespace MVC_Exercises.Controllers
{
    public class BooksController : Controller
    {
        // GET
        public IActionResult Index()
        {
            return View();
        }
    }
}