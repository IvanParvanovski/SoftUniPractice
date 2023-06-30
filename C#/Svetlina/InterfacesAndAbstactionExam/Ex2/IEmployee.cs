namespace Ex2
{
    public interface IEmployee
    {
        string FirstName { get; set; }
        string LastName { get; set; }
        string Department { get; set; }
        decimal Salary { get; set; }
        decimal GetSalary();
    }
}