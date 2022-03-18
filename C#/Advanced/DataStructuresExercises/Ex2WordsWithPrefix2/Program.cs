using System;
using rm.Trie;

namespace Ex2
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Trie trie = new Trie();
            string[] words = Console.ReadLine().Split(' ');
            string prefix = Console.ReadLine();

            foreach (string word in words)
            {
                trie.AddWord(word);    
            }

            Console.WriteLine(trie.Count());
            Console.WriteLine(trie.UniqueCount());
            Console.WriteLine(string.Join(", ", trie.GetWords()));
            Console.WriteLine(string.Join(", ", trie.GetWords(prefix)));
            trie.RemovePrefix(prefix);
            Console.WriteLine(string.Join(", ", trie.GetWords()));
        }
    }
}