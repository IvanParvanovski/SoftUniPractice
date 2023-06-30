namespace Ex1
{
    public class Member : Customer
    {
        public int MembershipId { get; set; }
        
        public Member(string firstName, string lastName, int membershipId) 
            : base(firstName, lastName)
        {
            this.MembershipId = membershipId;
        }

        public string GetMemberCard(string freeAccess)
        {
            return $"Member {this.FirstName} {this.LastName} with membership number {this.MembershipId} gets free access to the {freeAccess}.";
        }
    }
}