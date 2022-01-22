using System;
using System.Linq;

namespace ExTest
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Car audi = new Car("audi", 1990);
            
            Car bmw = new Car("bmw", 2010);
            Car mercedes = new Car("mercedes", 2020);
            Car ferrari = new Car("ferrari", 2016);
            Car apollo = new Car("apollo", 2016);

            DealerShip sofiaAuto = new DealerShip(bmw, mercedes, ferrari, apollo);

            foreach (var car in sofiaAuto.OrderBy(x => x))
            {
                Console.WriteLine(car);
            }
        }
    }
}