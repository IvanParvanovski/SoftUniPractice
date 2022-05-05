using System;
using System.Collections.Generic;

namespace Classbook.Models
{
    public partial class Student
    {
        public Student()
        {
            Grades = new HashSet<Grade>();
        }

        public int Id { get; set; }
        public string FirstName { get; set; } = null!;
        public string LastName { get; set; } = null!;
        public string StudentClass { get; set; } = null!;

        public virtual ICollection<Grade> Grades { get; set; }
    }
}
