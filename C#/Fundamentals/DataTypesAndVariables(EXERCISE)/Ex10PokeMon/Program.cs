using System;

namespace Ex10PokeMon
{
    class Program
    {
        static void Main(string[] args)
        {
            int startPokePower = int.Parse(Console.ReadLine());
            int distanceBetweenEnemies = int.Parse(Console.ReadLine());
            int exhaustionFactor = int.Parse(Console.ReadLine());
            int pokedTargets = 0;
            int pokePower = startPokePower;

            
            while (true)
            {
                if (pokePower == 50.0 / 100 * startPokePower)
                    if (exhaustionFactor != 0)
                        pokePower /= exhaustionFactor;

                if (pokePower < distanceBetweenEnemies)
                    break;

                pokePower -= distanceBetweenEnemies;
                pokedTargets++;
            }

            Console.WriteLine(pokePower);
            Console.WriteLine(pokedTargets);
        }
    }
}
