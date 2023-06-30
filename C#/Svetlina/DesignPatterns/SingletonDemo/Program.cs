// See https://aka.ms/new-console-template for more information

using System;

namespace SingletonDemo
{
    class Program
    {
        private static SingletonDataContainer instance = new SingletonDataContainer();
        public static SingletonDataContainer Instance => instance;
        
        public static void Main(string[] args)
        {
            // var db = SingletonDataContainer.Instance;
        }
    }
}