using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3Classification
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, string> contests = new Dictionary<string, string>();
            Dictionary<string, Dictionary<string, int>> candidates = new Dictionary<string, Dictionary<string, int>>();
            
            while (true)
            {
                string contest = Console.ReadLine();
                if (contest == "the contests are ended")
                {
                    break;
                }

                string[] contestData = contest.Split(":");
                contests[contestData[0]] = contestData[1];
            }

            while (true)
            {
                string candidate = Console.ReadLine();
                if (candidate == "the submissions are ended")
                {
                    break;
                }

                string[] candidateData = candidate.Split("=>");
                
                string searchedContest = candidateData[0];
                string candidatePassword = candidateData[1];
                string candidateName = candidateData[2];
                int candidatePoints = int.Parse(candidateData[3]);

                string contestPassword = "";
                if (contests.ContainsKey(searchedContest))
                {
                    contestPassword = contests[searchedContest];
                }

                if (contestPassword == candidatePassword)
                {
                    if (!candidates.ContainsKey(candidateName))
                    {
                        candidates[candidateName] = new Dictionary<string, int>();
                    }

                    if (candidates[candidateName].ContainsKey(searchedContest))
                    {
                        if (candidates[candidateName][searchedContest] < candidatePoints)
                        {
                            candidates[candidateName][searchedContest] = candidatePoints;
                        }
                    }
                    else
                    {
                        candidates[candidateName][searchedContest] = candidatePoints;
                    }
                }
            }

            var sortedCandidatesByPoints = candidates.OrderByDescending(x => x.Value.Values.Sum()).ToArray();
            var bestCandidate = sortedCandidatesByPoints[0];
            Console.WriteLine($"Candidate number one is {bestCandidate.Key} with total {bestCandidate.Value.Values.Sum()} points.");
            
            var sortedCandidatesByName = candidates.OrderBy(x => x.Key);
            Console.WriteLine("Ranking:");
            foreach (KeyValuePair<string, Dictionary<string, int>> candidateData in sortedCandidatesByName)
            {
                Console.WriteLine(candidateData.Key);
                var sortedCandidateContests = candidateData.Value.OrderByDescending(x => x.Value);
                
                foreach (KeyValuePair<string, int> contestData in sortedCandidateContests)
                {
                    Console.WriteLine($"#  {contestData.Key} -> {contestData.Value}");
                }
            }
        }
    }
}