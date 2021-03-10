namespace Ex5VehiclesCatalogue
{
    public class Vehicle
    {
        public string TypeOfVehicle { get; set; }
        public string Model { get; set; }
        public string Color { get; set; }
        public int HorsePower { get; set; }

        public override string ToString()
        {
            return $"Type: {TypeOfVehicle}\n" +
                   $"Model: {Model}\n" +
                   $"Color: {Color}\n" +
                   $"Horsepower: {HorsePower}";
        }
    }
}