namespace CarManufacturer
{
    public class Tire
    {
        private int year;
        private double pressure;
        
        public Tire(int year, double pressure)
        {
            this.Year = year;
            this.Pressure = pressure;
        }
        
        public int Year
        {
            get => year;
            set => year = value;
        }
        
        public double Pressure
        {
            get => pressure;
            set => pressure = value;
        }
    }
}