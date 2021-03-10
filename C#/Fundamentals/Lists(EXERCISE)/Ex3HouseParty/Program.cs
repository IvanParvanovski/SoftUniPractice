using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3HouseParty
{
    class Program
    {
        static void Main(string[] args)
        {
            HashSet<string> guests = new HashSet<string>();

            int commands = int.Parse(Console.ReadLine());

            for (int i = 0; i < commands; i++)
            {
                string[] user_data = Console.ReadLine().Split();
                string person = user_data[0];

                if (user_data.Contains("not"))
                {
                    guests = RemovePersonFromGuestList(guests, person);
                    continue;
                }

                guests = AddPersonToGuestList(guests, person);

            }

            Console.WriteLine(string.Join("\n", guests));

        }
        private static HashSet<string> RemovePersonFromGuestList(HashSet<string> guests,
                                                                 string person)
        {
            HashSet<string> guestList = guests.ToHashSet();

            if (DoesGuestListContainsPerson(guestList, person))
                guestList.Remove(person);
            else
                Console.WriteLine($"{person} is not in the list!");

            return guestList;
        }

        private static HashSet<string> AddPersonToGuestList(HashSet<string> guests, 
                                                            string person)
        {
            HashSet<string> guestList = guests.ToHashSet();

            if (!DoesGuestListContainsPerson(guestList, person))
                guestList.Add(person);
            else
                Console.WriteLine($"{person} is already in the list!");

            return guestList;
        }

        private static bool DoesGuestListContainsPerson(HashSet<string> guestList, string person)
        {
            return guestList.Contains(person);
        }


    }

}
