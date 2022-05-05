using System;
using System.Linq;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using VendingMachines.Models;

namespace VendingMachines.Controllers
{
    public class MachineController : Controller
    {
        private MachineContext _context;

        public MachineController(MachineContext dbCont)
        {
            _context = dbCont;
        }
        
        // GET
        public IActionResult MachineIndex()
        {
            ViewBag.MachinesList = _context.Machines.ToList();
            
            return View();
        }

        public IActionResult Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var machine = _context.Machines.Single(m => m.Id == id);

            if (machine == null)
            {
                return NotFound();
            }

            return View(machine);
        }

        public IActionResult Create()
        {
            return View();
        }
        
        // POST: Machine/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create([Bind("Id,Lat,Lon,PlacedAt,Type")] Machine machine)
        {
            _context.Machines.Add(machine);
            _context.SaveChanges();
            return RedirectToAction("MachineIndex");
        }
        
        // GET: Machine/Edit/5
        public IActionResult Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var machine = _context.Machines.Single(m => m.Id == id);
            if (machine == null)
            {
                return NotFound();
            }

            return View(machine);
        }
        
        // POST: Machine/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(int id, [Bind("Id,Lat,Lon,PlacedAt,Type")] Machine machine)
        {
            if (id != machine.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    _context.Update(machine);
                    _context.SaveChanges();
                }
                catch (DbUpdateException e)
                {
                    if (!MachineExists(machine.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }

                return RedirectToAction("MachineIndex");
            }

            return View(machine);
        }
        
        // GET: Machine/Delete/5
        public IActionResult Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var machine = _context.Machines.Single(m => m.Id == id);

            if (machine == null)
            {
                return NotFound();
            }

            return View(machine);
        }
        
        // POST: Machine/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public IActionResult DeleteConfirmed(int id)
        {
            var machine = _context.Machines.Single(m => m.Id == id);
            _context.Machines.Remove(machine);
            _context.SaveChanges();
            return RedirectToAction("MachineIndex");
        }

        private bool MachineExists(int id)
        {
            return _context.Machines.Any(m => m.Id == id);
        }
    }
}