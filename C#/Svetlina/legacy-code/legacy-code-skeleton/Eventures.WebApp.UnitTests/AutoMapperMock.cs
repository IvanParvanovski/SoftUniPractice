using AutoMapper;
using Eventures.Services.Infrastructure;
using Eventures.WebApp.Infrastructure;

namespace Eventures.WebApp.UnitTests
{
    public static class AutoMapperMock
    {
        public static IMapper Instance
        {
            get
            {
                MapperConfiguration config = new MapperConfiguration(cfg =>
                {
                    cfg.AddProfile(new ServiceMappingProfile());
                    cfg.AddProfile(new ControllerMappingProfile());
                });

                return new Mapper(config);
            }
        }
    }
}
