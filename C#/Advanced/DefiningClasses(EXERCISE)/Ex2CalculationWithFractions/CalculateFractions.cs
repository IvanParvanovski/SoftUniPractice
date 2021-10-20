using System;
using System.Collections.Generic;
using Fractions;

namespace Ex2CalculationWithFractions
{
    public class CalculateFractions
    {
        private readonly Fraction _f1;
        private readonly Fraction _f2;
        private readonly string _operation;
        private readonly Dictionary<string, Func<Fraction, Fraction, Fraction>> _operations = 
            new Dictionary<string, Func<Fraction, Fraction, Fraction>> 
        { 
            {"+", Sum},
            {"-", Subtract},
        };
        
        public CalculateFractions(Fraction f1, Fraction f2, string operation)
        {
            this._f1 = f1;
            this._f2 = f2;
            this._operation = operation;
        }
        public Fraction Calculate()
        {
            return _operations[_operation](this._f1, this._f2);
        }

        private static Fraction Sum(Fraction f1, Fraction f2)
        {
            return f1 + f2;
        }

        private static Fraction Subtract(Fraction f1, Fraction f2)
        {
            return f1 - f2;
        }

    }
}