using System;

using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;

namespace Eventures.Data
{
    public class ApplicationDbContext : IdentityDbContext<EventuresUser>
    {
        private bool seedDb = true;

        public ApplicationDbContext(
            DbContextOptions<ApplicationDbContext> options, bool seedDb = true)
            : base(options)
        {
            this.seedDb = seedDb;
            this.Database.EnsureCreated();
        }

        public DbSet<Event> Events { get; set; }

        private EventuresUser GuestUser { get; set; }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            if(seedDb)
            {
                SeedUsers();
                builder.Entity<EventuresUser>()
                    .HasData(this.GuestUser);

                builder
                    .Entity<Event>()
                    .HasData(new Event()
                    {
                        Id = 1,
                        Name = "Softuniada",
                        Place = "Sofia",
                        Start = DateTime.Parse(DateTime.Now.AddDays(200)
                            .ToString("yyyy-MM-dd HH:mm")), 
                        End = DateTime.Parse(DateTime.Now.AddDays(201)
                            .ToString("yyyy-MM-dd HH:mm")),
                        TotalTickets = 200,
                        PricePerTicket = 12.50M,
                        OwnerId = this.GuestUser.Id,
                        Description = "Come to our event in <b>Sofia</b> to participate in our <i>programming</i> challenge hosted by <u>SoftUni.</u>"
                    },
                    new Event()
                    {
                        Id = 2,
                        Name = "OpenFest",
                        Place = "Online",
                        Start = DateTime.Parse(DateTime.Now.AddDays(500)
                            .ToString("yyyy-MM-dd HH:mm")),
                        End = DateTime.Parse(DateTime.Now.AddDays(500).AddHours(8)
                            .ToString("yyyy-MM-dd HH:mm")),
                        TotalTickets = 500,
                        PricePerTicket = 10.00M,
                        OwnerId = this.GuestUser.Id,
                        Description = "<b>OpenFest</b> is an <i>online event</i> in which programmers all around the world big or small come to discuss the future of many languages including <u>C#, Java, JavaScript, Python</u> and many more! Join us and discuss the future of IT!"
                    },
                    new Event()
                    {
                        Id = 3,
                        Name = "Microsoft Build",
                        Place = "Online",
                        Start = DateTime.Parse(DateTime.Now.AddDays(300)
                            .ToString("yyyy-MM-dd HH:mm")),
                        End = DateTime.Parse(DateTime.Now.AddDays(300).AddHours(12)
                            .ToString("yyyy-MM-dd HH:mm")),
                        TotalTickets = 1000,
                        PricePerTicket = 0.00m,
                        OwnerId = this.GuestUser.Id,
                        Description = "Our <u>special seminar online</u> hosted by Microsoft will consist of topics involving the new release of <b>.NET 7</b>, updates to TypeScript and many more!"
                    });
            }

            base.OnModelCreating(builder);
        }

        private void SeedUsers()
        {
            PasswordHasher<EventuresUser> hasher = new PasswordHasher<EventuresUser>();

            this.GuestUser = new EventuresUser()
            {
                UserName = "guest",
                NormalizedUserName = "GUEST",
                Email = "guest@mail.com",
                NormalizedEmail = "GUEST@MAIL.COM",
                FirstName = "Guest",
                LastName = "User",
            };

            this.GuestUser.PasswordHash = hasher.HashPassword(this.GuestUser, "guest");
        }
    }
}
