using System.Collections;
using System.Collections.Generic;

namespace ExTest
{
    public class DealerShip : IEnumerable<Car>
    {
        public DealerShip(params Car[] cars)
        {
            this.Cars = new List<Car>(cars);
        }
        
        public IEnumerator<Car> GetEnumerator()
        {
            for (int i = 0; i < Cars.Count; i++)
            {
                yield return Cars[i];
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
        
        public List<Car> Cars { get; set; }

    }
}