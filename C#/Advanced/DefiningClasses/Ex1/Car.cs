namespace Ex1
{
    public class Car
    {
        private string _make;
        private string _model;
        private int _year;

        public Car()
        {
            
        }
        
        public Car(string make, string model, int year)
        {
            this.Make = make;
            this.Model = model;
            this.Year = year;
        }
        
        public string Make
        {
            get => _make;
            set => _make = value;
        }
        public string Model 
        { 
            get => _model;
            set => _model = value; 
        }
        public int Year
        {
            get => _year;
            set => _year = value;
        }
        
    }
}