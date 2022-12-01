using EntityRelations.Models;
using Microsoft.EntityFrameworkCore;

namespace EntityRelations
{
    public class OneToOneContext : DbContext
    {
        public virtual DbSet<Student> Students { get; set; }
        
        public virtual DbSet<Address> Addresses { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer(@"Server=(localdb)\mssqllocaldb;Database=OneToOne");
            }
        }
        
        
    }
}