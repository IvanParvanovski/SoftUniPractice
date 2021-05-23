using System;
using System.Numerics;
using System.Text;
using System.Text.RegularExpressions;

namespace IBAN
{
    class Program
    {
        static int mod(String num, int a)
        {
            // Initialize result
            int res = 0;
 
            // One by one process all
            // digits of 'num'
            for (int i = 0; i < num.Length; i++)
                res = (res * 10 + (int)num[i] - '0') % a;
 
            return res;
        }
        static bool CheckIBAN(string iban)
        {
            Match m = Regex.Match(iban, "^BG[0-9A-Z]{20}$");
            if (!m.Success)
            {
                return false;
            }
            
            string iban1 = iban.Substring(4) + iban.Substring(0, 4);
            StringBuilder sb = new StringBuilder();
            foreach (char sym in iban1)
            {
                if (char.IsUpper(sym))
                {
                    sb.Append(sym - 'A' + 10);
                }
                else
                {
                    sb.Append(sym);
                }
            }
            string iban2 = sb.ToString();
            
            /*if (mod(iban2, 97) != 1)
            {
                return false;
            }*/
            
            BigInteger num = BigInteger.Parse(iban2);
            if (num % 97 != 1)
            {
                return false;
            }
            return true;
        }
        
        static void Main(string[] args)
        {
            string iban = "BG80BNBG96611020345678";
            
            IBAN myIBAN = new IBAN(iban);
            
            Console.WriteLine(myIBAN.Validate());
            
            Console.WriteLine(CheckIBAN(iban));
        }
    }
}