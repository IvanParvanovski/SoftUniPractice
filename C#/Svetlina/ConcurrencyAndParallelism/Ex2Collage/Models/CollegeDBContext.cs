using System;
using Microsoft.EntityFrameworkCore;

namespace Ex2Collage.Models
{
	public class CollegeDBContext : DbContext
	{
		public CollegeDBContext()
		{
		}

		//protected override void OnConfiguration(DbContextOptionsBuilder optionsBuilder)
		//{
		//	if (!optionsBuilder.IsConfigured)
		//	{
		//		optionsBuilder.UseSqlServer();
		//	}
		//}
	}
}

