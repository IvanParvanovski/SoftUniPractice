using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Shopping_Center
{
    public class StartUp
    {
        private static readonly ProductList ProductList = new ProductList();
        private static readonly Dictionary<string, Func<string[], string>> COMMANDS = 
            new Dictionary<string, Func<string[], string>>
        {
            {"AddProduct", AddProduct},
            {"DeleteProducts", DeleteProducts},
            {"FindProductsByName", FindProductsByName},
            {"FindProductsByProducer", FindProductsByProducer},
            {"FindProductsByPriceRange", FindProductsByPriceRange},
        };
        
        public static void Main()
        {
            var count = int.Parse(Console.ReadLine()!);

            for (var i = 0; i < count; i++)
            {
                var command = Console.ReadLine()!;
                ProcessCommand(command);
            }
        }

        private static void ProcessCommand(string input)
        {
            input = input.Trim();
            
            int index = input.IndexOf(' ');
            string command = input.Substring(0, index);
            
            input = input.Substring(index + 1);
            string[] args = input.Split(new[] { ';' }, StringSplitOptions.RemoveEmptyEntries);
            
            string result = !COMMANDS.ContainsKey(command) ? "Invalid Command" : COMMANDS[command](args);
            Console.WriteLine(result);
        }

        private static string FindProductsByPriceRange(string[] args)
        {
            decimal fromPrice = Decimal.Parse(args[0]);
            decimal toPrice = Decimal.Parse(args[1]);
            var result = ProductList.FindProductsByPriceRange(fromPrice, toPrice);
            
            return ConcatenateProducts(result);
        }

        private static string FindProductsByProducer(string[] args)
        {
            string producer = args[0];
            var result = ProductList.FindProductsProducer(producer);
            
            return ConcatenateProducts(result);
        }

        private static string FindProductsByName(string[] args)
        {
            string name = args[0];
            var result = ProductList.FindProductsByName(name);

            return ConcatenateProducts(result);
        }
        
        private static string ConcatenateProducts(IEnumerable<Product> products)
        {
            if (!products.Any()) { return "No products found"; }

            var orderedEnumerable = products.OrderBy(x => x.Name)
                .ThenBy(x => x.Producer)
                .ThenBy(x => x.Price);

            return String.Join("\n", orderedEnumerable);
        }

        private static string DeleteProducts(string[] args)
        {
            int result;
            if (args.Length == 1)
            {
                string producer = args[0]; 
                result = ProductList.DeleteByProducer(producer);
            }
            else
            {
                string name = args[0];
                string producer = args[1];
                result = ProductList.DeleteByNameAndProducer(name, producer);
            }

            if (result == 0)
            {
                return "No products found";
            }
            
            return $"{result} products deleted";
        }

        private static string AddProduct(string[] args)
        {
            string name = args[0];
            decimal price = Decimal.Parse(args[1]);
            string producer = args[2];
            ProductList.AddProduct(name, price, producer);
            
            return "Product added";
        }
    }
}
