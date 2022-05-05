FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["ParkingApp/ParkingApp.csproj", "ParkingApp/"]
RUN dotnet restore "ParkingApp/ParkingApp.csproj"
COPY . .
WORKDIR "/src/ParkingApp"
RUN dotnet build "ParkingApp.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ParkingApp.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ParkingApp.dll"]
