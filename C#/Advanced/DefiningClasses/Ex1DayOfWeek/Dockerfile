FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1DayOfWeek/Ex1DayOfWeek.csproj", "Ex1DayOfWeek/"]
RUN dotnet restore "Ex1DayOfWeek/Ex1DayOfWeek.csproj"
COPY . .
WORKDIR "/src/Ex1DayOfWeek"
RUN dotnet build "Ex1DayOfWeek.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1DayOfWeek.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1DayOfWeek.dll"]
