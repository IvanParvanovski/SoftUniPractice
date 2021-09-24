FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1Names/Ex1Names.csproj", "Ex1Names/"]
RUN dotnet restore "Ex1Names/Ex1Names.csproj"
COPY . .
WORKDIR "/src/Ex1Names"
RUN dotnet build "Ex1Names.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1Names.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1Names.dll"]
