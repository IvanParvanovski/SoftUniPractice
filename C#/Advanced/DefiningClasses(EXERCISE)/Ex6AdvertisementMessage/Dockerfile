FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex6AdvertisementMessage/Ex6AdvertisementMessage.csproj", "Ex6AdvertisementMessage/"]
RUN dotnet restore "Ex6AdvertisementMessage/Ex6AdvertisementMessage.csproj"
COPY . .
WORKDIR "/src/Ex6AdvertisementMessage"
RUN dotnet build "Ex6AdvertisementMessage.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex6AdvertisementMessage.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex6AdvertisementMessage.dll"]
