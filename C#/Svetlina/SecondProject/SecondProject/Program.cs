
// See https://aka.ms/new-console-template for more information

using SecondProject.Data;
using SecondProject.Models;

using ContosoPizzaContext context = new ContosoPizzaContext();

Product veggieSpecial = new Product()
{
    Name = "Veggie Special Pizza",
    Price = 9.99M
};

context.Products.Add(veggieSpecial); 

Product deluceMeat = new Product()
{
    Name = "Deluxe Meat Pizza",
    Price = 12.99M
};

context.Add(deluceMeat);

context.SaveChanges();

// var products = context.Products.Where(p => p.Price > 10.00M).OrderBy(p => p.Name);

foreach (Product p in products)
{
    Console.WriteLine($"Id:    {p.Id}");
    Console.WriteLine($"Name:  {p.Name}");
    Console.WriteLine($"Price: {p.Price}");
    Console.WriteLine(new string('-', 20));
}