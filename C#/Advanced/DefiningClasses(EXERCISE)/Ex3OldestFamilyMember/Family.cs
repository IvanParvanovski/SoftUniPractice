using System.Collections.Generic;
using System.Linq;

namespace DefiningClasses
{
    public class Family
    {
        private List<Person> people = new List<Person>();

        public void AddMember(Person member)
        {
            people.Add(member);
        }

        public Person GetOldestMember()
        {
            Person oldestMember = this.people[0];

            foreach (var member in this.people)
            {
                if (member.Age > oldestMember.Age)
                {
                    oldestMember = member;
                }
            }

            return oldestMember;
        }
    }
}