using System.Collections.Generic;

namespace Prototype
{
    public class SandwichMenu
    {
        private Dictionary<string, SandwichPrototype> sandwiches = new Dictionary<string, SandwichPrototype>();

        public SandwichPrototype this[string name]
        {
            get { return sandwiches[name]; }
            set {sandwiches.Add(name, value); }
        }
    }
}