using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace VendingMachines.Models
{
    public partial class MachineContext : DbContext
    {
        public MachineContext()
        {
        }

        public MachineContext(DbContextOptions<MachineContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Machine> Machines { get; set; } = null!;

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see http://go.microsoft.com/fwlink/?LinkId=723263.
                optionsBuilder.UseSqlServer("Server=(localdb)\\MSSQLLocalDB;Database=VendingMachines;Integrated Security=true;");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Machine>(entity =>
            {
                entity.ToTable("Machine");

                entity.Property(e => e.Lat)
                    .HasMaxLength(30)
                    .HasColumnName("LAT");

                entity.Property(e => e.Lon)
                    .HasMaxLength(30)
                    .HasColumnName("LON");

                entity.Property(e => e.PlacedAt).HasColumnType("datetime");

                entity.Property(e => e.Type).HasMaxLength(30);
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
