FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1Car/Ex1Car.csproj", "Ex1Car/"]
RUN dotnet restore "Ex1Car/Ex1Car.csproj"
COPY . .
WORKDIR "/src/Ex1Car"
RUN dotnet build "Ex1Car.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1Car.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1Car.dll"]
