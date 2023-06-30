// See https://aka.ms/new-console-template for more information

using System;

namespace Ex1
{
    public class StartUp
    {
        public static void Main(string[] args)
        {
            string input = Console.ReadLine();
            int row = 1;
            
            while (input != "End")
            {
                string[] data = input.Split(" ");
                string firstName = data[0];
                string lastName = data[1];

                if (data.Length == 2)
                {
                    Guest guest = new Guest(firstName, lastName);
                    guest.FirstName = firstName;
                    guest.LastName = lastName;
                    Console.WriteLine(guest.NewGuest());
                }
                else if (data.Length == 3)
                {
                    int membershipId = int.Parse(data[2]);
                    Member member = new Member(firstName, lastName, membershipId);
                    if (row % 2 == 0)
                    {
                        Console.WriteLine(member.GetMemberCard("fitness"));
                    }
                    else
                    {
                        Console.WriteLine(member.GetMemberCard("spa"));
                    }
                }
                else if (data.Length == 4)
                {
                    string department = data[2];
                    int employeeId = int.Parse(data[3]);

                    Employee employee = new Employee(firstName, lastName, department, employeeId);
                    Console.WriteLine(employee.StartWorkingDay());
                }
                
                input = Console.ReadLine();
                row++;
            }
        }
    }
}