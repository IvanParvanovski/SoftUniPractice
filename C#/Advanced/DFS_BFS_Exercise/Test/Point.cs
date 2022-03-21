namespace Ex2Maze
{
    public class Point
    {
        public int X { get; set; }
        public int Y { get; set; }
        
        public Point PreviousPoint { get; set; }
        
        public string Direction { get; set; }

        public Point(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }
    }
}