FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1Dates/Ex1Dates.csproj", "Ex1Dates/"]
RUN dotnet restore "Ex1Dates/Ex1Dates.csproj"
COPY . .
WORKDIR "/src/Ex1Dates"
RUN dotnet build "Ex1Dates.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1Dates.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1Dates.dll"]
