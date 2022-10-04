// See https://aka.ms/new-console-template for more information

using System;

namespace Bank
{
    class BankAccount
    {
        public string CustomerName { get; set; }
        public decimal Balance { get; set; }

        public BankAccount(string name, decimal initialBalance)
        {
            CustomerName = name;
            Balance = initialBalance;
        }

        public void DepositTransaction(decimal cash)
        {
            Balance += cash;
        }

        public void WithdrawalTransaction(decimal cash)
        {
            Balance -= cash;
        }

        public override string ToString()
        {
            return $"Dear {CustomerName}, your balance is: {Balance}";
        }
    } 
    
    class Program
    {
        public static void Main(string[] args)
        {
            
        }
    }
}