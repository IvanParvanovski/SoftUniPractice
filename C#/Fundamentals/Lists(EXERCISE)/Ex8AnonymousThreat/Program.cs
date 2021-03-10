using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex8AnonymousThreat
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> elements = Console.ReadLine().Split().ToList();

            while (true)
            {
                string user_input = Console.ReadLine();

                if (user_input == "3:1")
                    break;

                string[] data = user_input.Split();
                string command = data[0];

                if (command == "merge")
                {
                    int startIndex = int.Parse(data[1]);
                    int endIndex = int.Parse(data[2]);

                    if (startIndex < 0)
                        startIndex = 0;

                    else if (endIndex > elements.Count())
                        endIndex = elements.Count() - 1;

                    for (int i = startIndex; i < endIndex - 1; i++)
                    {
                        string currentText = elements[startIndex];
                        string nextText = elements[startIndex + 1];
                        elements.RemoveAt(startIndex);
                        elements.RemoveAt(startIndex);
                        elements.Insert(startIndex, currentText + nextText);
                    }
                }

                else if (command == "divide")
                {
                    int index = int.Parse(data[1]);
                    int partions = int.Parse(data[2]);

                    string text = elements[index];
                    elements.RemoveAt(index);

                    string word = "";
                    for (int i = 0; i < text.Length; i++)
                    {
                        word += text[i];

                        if (i % partions == 0)
                        {
                            elements.Insert(index, word);
                            word = "";
                            index++;
                        }
                    }
                }
            }
            Console.WriteLine(string.Join(" ", elements));
        }
    }
}
