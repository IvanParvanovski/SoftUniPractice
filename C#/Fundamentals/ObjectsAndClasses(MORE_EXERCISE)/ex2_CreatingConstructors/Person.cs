using System.Collections.Generic;

namespace ex2_CreatingConstructors
{
    public class Person : IPerson
    {
        private List<Person> _members { get; set; }

        public List<Person> Members
        {
            get => _members;
            set => _members = value;
        }

        public Family()
        {
            this.Members = new List<Person>();
        }

        public void AddMember(Person person)
        {
            this.Members.Add(person);
        } 

        public string Name { get; set; }
        public int Age { get; set; }

        public Person()
        {
            this.Age = 1;
            this.Name = "No name";
        }

        public Person(int age)
        {
            this.Age = age;
            this.Name = "No name";
        }

        public Person(string name, int age)
        {
            this.Age = age;
            this.Name = name;
        }

    }
}