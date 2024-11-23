using System;
using System.Globalization;
using AutoMapper;

using Eventures.Data;
using Eventures.Services.Models;

namespace Eventures.Services.Infrastructure
{
	public class ServiceMappingProfile : Profile
	{
		public ServiceMappingProfile()
		{
			this.CreateMap<Event, EventServiceModel>()
				.ForMember(esm => esm.Start,
					cfg => cfg.MapFrom(ev => ev.Start.ToString("dd-MM-yyyy HH:mm", CultureInfo.InvariantCulture)))
				.ForMember(esm => esm.End,
					cfg => cfg.MapFrom(ev => ev.End.ToString("dd-MM-yyyy HH:mm", CultureInfo.InvariantCulture)));
			
		}
    }
}

