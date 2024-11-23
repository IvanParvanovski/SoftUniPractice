namespace GreadyActivitySelection
{
    public class Program
    {
        static void Main()
        {
            // Example data for the activity selection problem
            List<Activity> activities = new List<Activity>
        {
            new Activity("A1", 0, 6),
            new Activity("A2", 3, 4),
            new Activity("A3", 1, 2),
            new Activity("A4", 5, 8),
            new Activity("A5", 5, 7),
            new Activity("A6", 8, 9),
        };

            List<Activity> selectedActivities = GreedyActivitySelection(activities);

            // Display the selected activities
            Console.WriteLine("Selected Activities:");
            foreach (var activity in selectedActivities)
            {
                Console.WriteLine($"{activity.Name} - Start: {activity.StartTime}, End: {activity.EndTime}");
            }
        }

        static List<Activity> GreedyActivitySelection(List<Activity> activities)
        {
            // Sort activities by their end times
            List<Activity> sortedActivities = activities.OrderBy(a => a.EndTime).ToList();

            List<Activity> selectedActivities = new List<Activity>();
            Activity previousActivity = null;

            foreach (var currentActivity in sortedActivities)
            {
                // Include the first activity and any activity that starts after the previous one ends
                if (previousActivity == null || currentActivity.StartTime >= previousActivity.EndTime)
                {
                    selectedActivities.Add(currentActivity);
                    previousActivity = currentActivity;
                }
            }

            return selectedActivities;
        }
    }

    class Activity
    {
        public string Name { get; }
        public int StartTime { get; }
        public int EndTime { get; }

        public Activity(string name, int startTime, int endTime)
        {
            Name = name;
            StartTime = startTime;
            EndTime = endTime;
        }
    }
}
