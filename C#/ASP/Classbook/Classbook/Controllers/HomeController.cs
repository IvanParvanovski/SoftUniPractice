using System;
using System.Diagnostics;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using Classbook.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;

namespace Classbook.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly SchoolReportContext _context;
        
        public HomeController(ILogger<HomeController> logger, SchoolReportContext dbCont)
        {
            _logger = logger;
            _context = dbCont;
        }

        public IActionResult Index()
        {
            var students = _context.Students.Include(x =>x.Grades).ToList();

            ViewBag.Students = students;
            
            return View(students);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel {RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier});
        }
    }
}

