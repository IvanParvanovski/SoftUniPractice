using Forum.Models;
using Microsoft.EntityFrameworkCore;

namespace Forum.Data
{
    public class ForumDbContext : DbContext
    {
        public ForumDbContext()
        {
        }

        public ForumDbContext(DbContextOptions<ForumDbContext> options)
            : base(options)
        {
        }
        public DbSet<Post> Posts { get; set; }
        public DbSet<PostAnswer> PostAnswers { get; set; }
        public DbSet<User> Users { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer("Server=(localdb)\\MSSQLLocalDB;Database=Forum;Integrated Security=True;");
            }
        }


        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Post>(entity =>
            {
                entity.HasOne(d => d.User)
                 .WithMany(p => p.Posts)
                 .HasForeignKey(d => d.UserId);
            });
            modelBuilder.Entity<PostAnswer>(entity =>
            {
                entity.HasOne(d => d.Post)
                 .WithMany(p => p.PostAnswers)
                 .HasForeignKey(d => d.PostId);
            });

        }
    }
}
