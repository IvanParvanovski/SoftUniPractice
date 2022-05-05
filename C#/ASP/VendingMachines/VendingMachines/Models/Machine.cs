using System;
using System.Collections.Generic;

namespace VendingMachines.Models
{
    public partial class Machine
    {
        public int Id { get; set; }
        public string? Lat { get; set; }
        public string? Lon { get; set; }
        public DateTime? PlacedAt { get; set; }
        public string? Type { get; set; }
    }
}
