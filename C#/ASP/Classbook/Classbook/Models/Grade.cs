using System;
using System.Collections.Generic;

namespace Classbook.Models
{
    public partial class Grade
    {
        public int Id { get; set; }
        public int StudentId { get; set; }
        public double Grade1 { get; set; }

        public virtual Student Student { get; set; } = null!;
    }
}
