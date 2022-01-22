using System;
using System.Collections;
using System.Collections.Generic;

namespace Ex1Competitor
{
    class Competitor<T> 
        : IEnumerable<T>, IComparable<Competitor<T>>
    {
        private string _name;
        private int _age;
        private List<T> _scores;
        
        public Competitor(string name, int age)
        {
            Name = name;
            Age = age;
            Scores = new List<T>();
        }
        public void Add(T score)
        {
            Scores.Add(score);
        }
        
        public int CountCompetitions()
        {
            return Scores.Count;
        }
        
        public T ChangeLastScore(T newScore)
        {
            int n = Scores.Count - 1;
            T lastScore = Scores[n];
            Scores[n] = newScore;
            
            return lastScore;
        }
        
        public string Name
        { 
            get => _name;
            set => _name = value;
        }
        
        public int Age
        {
            get => _age;
            set
            {
                if (value < 10)
                {
                    throw new ArgumentOutOfRangeException("Age cannot be less than 10.");
                }
 
                _age = value;
            }
        }
        
        public List<T> Scores
        {
            get => _scores;
            set => _scores = value;
        }
 
        public IEnumerator<T> GetEnumerator()
        {
            for (int i = 0; i < Scores.Count; i++)
            {
                yield return Scores[i];
            }
        }
 
        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
 
        public int CompareTo(Competitor<T> other)
        {
            int result = Name.CompareTo(other.Name);
 
            if (result == 0)
            {
                result = Age.CompareTo(other.Age);
            }
 
            return result;
        }
    }
    
    internal class Program
    {
        public static void Main(string[] args)
        {
            Competitor<int> IvanTheWiner = new Competitor<int>("Ivan", 16);
            Competitor<int> Vanya = new Competitor<int>("Vanya", 17);
            IvanTheWiner.Add(6);
            IvanTheWiner.Add(2);
            IvanTheWiner.Add(5);
            IvanTheWiner.Add(4);
            Console.WriteLine(IvanTheWiner.CompareTo(Vanya));
        }
        
    }
}