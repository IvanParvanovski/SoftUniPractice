namespace Ex1
{
    public class Guest : Customer
    {
        public Guest(string firstName, string lastName) 
            : base(firstName, lastName)
        {
        }
       
        public string NewGuest()
        {
            return $"Mr/Ms/Mrs {FirstName} {LastName} registers as a guest.";
        }

        
    }
}