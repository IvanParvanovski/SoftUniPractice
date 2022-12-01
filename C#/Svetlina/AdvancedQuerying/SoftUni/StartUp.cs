using Microsoft.EntityFrameworkCore;
using SoftUni.Data;
using System;
using System.Linq;
using System.Text;
using Z.EntityFramework.Plus;

namespace SoftUni
{
    public class StartUp
    {
        static void Main()
        {
            var context = new SoftUniContext();
           
            
        }
        public static string AddEmployeeToProject(SoftUniContext context, int employeeId, int projectId)
        {
           
        }
        public static string DeleteRecordsWithProjectId(SoftUniContext context, int projectId)
        {
            
        }

    }
}
