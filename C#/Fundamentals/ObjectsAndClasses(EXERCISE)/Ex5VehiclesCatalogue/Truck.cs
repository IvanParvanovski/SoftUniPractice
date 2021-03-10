namespace Ex5VehiclesCatalogue
{
    public class Truck : Vehicle
    {
        public Truck(string model, string color, int horsePower)
        {
            this.TypeOfVehicle = "Truck"; 
            this.Model = model;
            this.Color = color;
            this.HorsePower = horsePower;
        }
    }
}