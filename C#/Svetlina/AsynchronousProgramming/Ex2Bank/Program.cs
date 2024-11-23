namespace Ex2Bank
{
    class Account
    {
        public int Balance { get; set; }

        public Account(int balance)
        {
            this.Balance = balance;

        }

        public int Withdraw(int amount)
        {
            if (this.Balance < 0)
            {
                throw new Exception("Negative Balance");
            }

            if (this.Balance >= amount)
            {
                Console.WriteLine($"Balance before withdraw: {Balance}");
                Console.WriteLine($"Amount to withdraw: -{amount}");
                this.Balance -= amount;
                Console.WriteLine($"Balance after withdraw: ${this.Balance}");
                return amount;
            }

            return 0;
        }

    }

    public class Program
    {
        public static void Main(string[] args)
        {
            var myAccount = new Account(500);

            var thread1 = Task.Run(() => myAccount.Withdraw(100));
            var thread2 = Task.Run(() => myAccount.Withdraw(100));
            var thread3 = Task.Run(() => myAccount.Withdraw(100));
            var thread4 = Task.Run(() => myAccount.Withdraw(100));
            var thread5 = Task.Run(() => myAccount.Withdraw(100));
            var thread6 = Task.Run(() => myAccount.Withdraw(100));
            var thread7 = Task.Run(() => myAccount.Withdraw(100));
            var thread8 = Task.Run(() => myAccount.Withdraw(100));
            var thread9 = Task.Run(() => myAccount.Withdraw(100));
            var thread10 = Task.Run(() => myAccount.Withdraw(100));

        }

    }
}