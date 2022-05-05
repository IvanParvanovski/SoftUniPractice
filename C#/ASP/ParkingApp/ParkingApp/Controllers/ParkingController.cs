using System;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ParkingApp.Models;

namespace ParkingApp.Controllers
{
    public class ParkingController : Controller
    {
        private ParkingContext _context;
        
        public ParkingController(ParkingContext dbCont)
        {
            _context = dbCont;
        }
        
        // GET
        public IActionResult ParkIndex()
        {
            ViewBag.CarList = _context.ParkInfos.ToList();
            return View();
        }
        
        // GET: Parking/Details/5
        public IActionResult Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var car = _context.ParkInfos.Single(m => m.Id == id);
            if (car == null)
            {
                return NotFound();
            }

            return View(car);
        }
        
        // GET: Parking/Create
        public IActionResult Create()
        {
            return View();
        }
        
        // POST: Parking/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create([Bind("Id,PlateNumber,ArrivedAt,PayedUntil")]ParkInfo car)
        {
            if (ModelState.IsValid)
            {
                if (car.PayedUntil - car.ArrivedAt < new TimeSpan(10, 0, 0))
                {
                    _context.ParkInfos.Add(car);
                    _context.SaveChanges();
                    return RedirectToAction("ParkIndex");
                }

                return BadRequest();
            }
            return View(car);
        }
        
        // GET: Parking/Edit/5
        public IActionResult Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var car = _context.ParkInfos.Single(m => m.Id == id);
            if (car == null)
            {
                return NotFound();
            }
            return View(car);
        }
        
        // POST: Parking/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(int id, [Bind("Id,PlateNumber,ArrivedAt,PayedUntil")] ParkInfo car)
        {
            if (id != car.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(car);
                    _context.SaveChanges();
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!CarExists(car.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction("ParkIndex");
            }
            return View(car);
        }
        
        // GET: Parking/Delete/5
        public IActionResult Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var car = _context.ParkInfos.Single(m => m.Id == id);
            if (car == null)
            {
                return NotFound();
            }

            return View(car);
        }
        
        // POST: Parking/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(int id)
        {
            var car = _context.ParkInfos.Single(m => m.Id == id);
            _context.ParkInfos.Remove(car);
            _context.SaveChanges();
            return RedirectToAction("ParkIndex");
        }
        
        private bool CarExists(int id)
        {
            return _context.ParkInfos.Any(e => e.Id == id);
        }
    }
}