// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;

namespace Ex2CreateClass
{
    public class Competitor<T>
    {
        public string Name { get; set; }
        private int age;
        public int Age
        {
            get
            {
                return age;
            }
            set
            {
                if (value < 10)
                {
                    throw new ArgumentOutOfRangeException("Age cannot be less than 10.");
                }

                age = value;
            }
        }
        public List<T> Scores { get; set; }

        public Competitor(string name, int age)
        {
            this.Name = name;
            this.Age = age;
            this.Scores = new List<T>();
        }
        
        public void Add(T score)
        {
            this.Scores.Add(score);
        }

        public int CountCompetitions()
        {
            return this.Scores.Count;
        }

        public T ChangeLastScore(T newScore)
        {
            int lastIndex = this.Scores.Count - 1;
            T lastScore = this.Scores[lastIndex];
            this.Scores.RemoveAt(lastIndex);
            this.Scores.Add(newScore);
            return lastScore;
        }
    }
    
    public class Program
    {
        public static void Main(string[] args)
        {
            Competitor<int> IvanTheWinner = new Competitor<int>("Ivan", 15);
            IvanTheWinner.Add(50);
            IvanTheWinner.Add(50);
            Console.WriteLine(IvanTheWinner.CountCompetitions());
            IvanTheWinner.ChangeLastScore(20);
            Console.WriteLine(IvanTheWinner.CountCompetitions());
        }
    }
}