namespace BookShop.Data
{
    internal class Configuration
    {
        //Check if the server name in the path is the same like in Microsoft SQL Management Studio.
        internal static string ConnectionString
            => @"Server=(localdb)\MSSQLLocalDB;Database=BookShop;Integrated Security=True;";
    }
}
