using System;
using System.Text;

namespace IBAN
{
    public class IBAN
    {
        public string UserIBAN { get; set; }
        
        public IBAN(string userIban)
        {
            this.UserIBAN = userIban;
        }
        private int mod(String num, int a)
        {
            int res = 0;
            
            for (int i = 0; i < num.Length; i++)
                res = (res * 10 + (int)num[i] - '0') % a;
 
            return res;
        }
        
        private static string GetNumericValueOfIbanWithLetters(string text)
        {
            string ibanRotated = text.Substring(4) + text.Substring(0, 4);
            StringBuilder result = new StringBuilder();
            
            foreach (char symbol in ibanRotated)
            {
                if (Char.IsDigit(symbol))
                    result.Append(symbol);
                else
                    result.Append(symbol - 'A' + 10);
            }

            return result.ToString();
        }

        private static string GetNumericValueOfIbanWithZeros(string text)
        {
            StringBuilder result = new StringBuilder(text);
            result[2] = '0';
            result[3] = '0';
            return GetNumericValueOfIbanWithLetters(result.ToString());
        }
        
        private static bool DoesStartWithBg(string text)
        {
            return text.StartsWith("BG");
        }
        
        private bool DoesModeEqualToOne(string text)
        {
            return mod(GetNumericValueOfIbanWithLetters(text), 97) == 1;
        }
        
        private static bool IsRightLength(string text)
        {
            return text.Length == 22;
        }
        
        private bool IsCheckNumberValid(string text)
        {
            string num = GetNumericValueOfIbanWithZeros(text);
            int value = mod(num, 97);
            return 98 - value == 1;
        }
        
        public bool Validate()
        {
            if (!IsRightLength(this.UserIBAN))
                return false;
            
            if (!DoesStartWithBg(this.UserIBAN))
                return false;

            if (!DoesModeEqualToOne(this.UserIBAN))
                return false;

            if (!IsCheckNumberValid(this.UserIBAN))
                return false;
            
            return true;
        }
    }
}