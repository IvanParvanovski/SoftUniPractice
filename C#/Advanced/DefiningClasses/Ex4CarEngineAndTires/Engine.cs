namespace CarManufacturer
{
    public class Engine
    {
        private int horsePower;
        private double cubicCapacity;

        public Engine(int horsePower, double cubicCapacity)
        {
            this.HorsePower = horsePower;
            this.CubicCapacity = cubicCapacity;
        }

        public int HorsePower
        {
            get => horsePower;
            set => horsePower = value;
        }

        public double CubicCapacity
        {
            get => cubicCapacity;
            set => cubicCapacity = value;
        }
    }
}