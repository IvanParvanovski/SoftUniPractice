namespace Ex5VehiclesCatalogue
{
    public class Car : Vehicle
    {
        public Car(string model, string color, int horsePower)
        {
            this.TypeOfVehicle = "Car"; 
            this.Model = model;
            this.Color = color;
            this.HorsePower = horsePower;
        }
    }
}