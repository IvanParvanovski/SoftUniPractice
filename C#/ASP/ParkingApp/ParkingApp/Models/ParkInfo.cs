using System;
using System.Collections.Generic;

namespace ParkingApp.Models
{
    public partial class ParkInfo
    {
        public int Id { get; set; }
        public string? PlateNumber { get; set; }
        public DateTime? ArrivedAt { get; set; }
        public DateTime? PayedUntil { get; set; }
    }
}
