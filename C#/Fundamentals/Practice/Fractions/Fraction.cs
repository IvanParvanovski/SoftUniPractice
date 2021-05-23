using System;

namespace Fractions
{
    public class Fraction
    {
        private int Numerator { get; set; }
        private int Denominator { get; set; }

        public Fraction(int numerator,
            int denominator)
        {
            this.Numerator = numerator;
            this.Denominator = denominator;
        }
        
        public override string ToString()
        {
            if (this.Numerator == 1 && this.Denominator == 1)
                return this.Numerator.ToString();
            return $"{this.Numerator}/{this.Denominator}";
        }
        private static int GCD(int a, int b)
        {
            while (b != 0)
            {
                int oldB = b;
                b = a % b;
                a = oldB;
            }
            return a;
        }

        public static Fraction operator *(Fraction fr1, Fraction fr2)
        {
            int newNumerator = fr1.Numerator * fr2.Numerator;
            int newDenominator = fr1.Denominator * fr2.Denominator;

            int gcd = GCD(newNumerator, newDenominator);
            newNumerator /= gcd;
            newDenominator /= gcd;
            
            return new Fraction(newNumerator, newDenominator);
        }

        public static Fraction operator /(Fraction fr1, Fraction fr2)
        {
            Fraction newFraction = fr1 * new Fraction(fr2.Denominator, fr2.Numerator);
            
            int gcd = GCD(newFraction.Numerator, newFraction.Denominator);
            newFraction.Numerator /= gcd;
            newFraction.Denominator /= gcd;
            
            return newFraction;
        }

        public static Fraction operator +(Fraction fr1, Fraction fr2)
        {
            int newNumerator = fr1.Numerator * fr2.Denominator +
                               fr2.Numerator * fr1.Denominator;
            
            int newDenominator = fr1.Denominator * fr2.Denominator;

            int gcd = GCD(newNumerator, newDenominator);
            newNumerator /= gcd;
            newDenominator /= gcd;
            
            return new Fraction(newNumerator, newDenominator);
        }
        
        public static Fraction operator -(Fraction fr1, Fraction fr2)
        {
            int newNumerator = fr1.Numerator * fr2.Denominator -
                               fr2.Numerator * fr1.Denominator;
            
            int newDenominator = fr1.Denominator * fr2.Denominator;

            int gcd = GCD(newNumerator, newDenominator);

            newNumerator /= gcd;
            newDenominator /= gcd;
            
            return new Fraction(newNumerator, newDenominator);
        }

        public static bool operator >(Fraction fr1, Fraction fr2)
        {
            int newNumeratorFr1 = fr1.Numerator * fr2.Denominator;
            int newNumeratorFr2 = fr2.Numerator * fr1.Denominator;

            return newNumeratorFr1 > newNumeratorFr2;
        }

        public static bool operator <(Fraction fr1, Fraction fr2)
        {
            int newNumeratorFr1 = fr1.Numerator * fr2.Denominator;
            int newNumeratorFr2 = fr2.Numerator * fr1.Denominator;

            return newNumeratorFr1 < newNumeratorFr2;
        }

        public static bool operator >=(Fraction fr1, Fraction fr2)
        {
            int newNumeratorFr1 = fr1.Numerator * fr2.Denominator;
            int newNumeratorFr2 = fr2.Numerator * fr1.Denominator;

            return newNumeratorFr1 >= newNumeratorFr2;
        }

        public static bool operator <=(Fraction fr1, Fraction fr2)
        {
            int newNumeratorFr1 = fr1.Numerator * fr2.Denominator;
            int newNumeratorFr2 = fr2.Numerator * fr1.Denominator;

            return newNumeratorFr1 <= newNumeratorFr2;
        }
            
        public static bool operator ==(Fraction fr1, Fraction fr2)
        {
            double fr1Value = (double) fr1!.Numerator / fr1.Denominator;
            double fr2Value = (double) fr2!.Numerator / fr2.Denominator;

            if (Math.Abs(fr1Value - fr2Value) < 0.001)
            {
                return true;
            }

            return false;
        }

        public static bool operator !=(Fraction fr1, Fraction fr2)
        {
            double fr1Value = (double) fr1!.Numerator / fr1.Denominator;
            double fr2Value = (double) fr2!.Numerator / fr2.Denominator;

            if (Math.Abs(fr1Value - fr2Value) < 0.001)
            {
                return false;
            }

            return true;
        }
    }
}