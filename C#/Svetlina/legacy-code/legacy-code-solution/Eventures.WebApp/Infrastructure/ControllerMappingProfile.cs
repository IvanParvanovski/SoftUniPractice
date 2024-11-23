using AutoMapper;

using Eventures.Services.Models;
using Eventures.WebApp.Models;

namespace Eventures.WebApp.Infrastructure
{
    public class ControllerMappingProfile : Profile
    {
        public ControllerMappingProfile()
        {
            this.CreateMap<EventServiceModel, EventViewModel>();
            this.CreateMap<EventServiceModel, EventBindingModel>();
        }
    }
}
