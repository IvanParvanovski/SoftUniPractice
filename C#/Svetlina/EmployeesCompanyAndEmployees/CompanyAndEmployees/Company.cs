using System;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Serialization;

namespace CompanyAndEmployees
{
    public class Company
    {
        public Company()
        {
            Employees = new List<Employee>();
        }

        public List<Employee> Employees { get; set; }
    }
}
