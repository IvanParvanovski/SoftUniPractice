FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex2ReadAndCount/Ex2ReadAndCount.csproj", "Ex2ReadAndCount/"]
RUN dotnet restore "Ex2ReadAndCount/Ex2ReadAndCount.csproj"
COPY . .
WORKDIR "/src/Ex2ReadAndCount"
RUN dotnet build "Ex2ReadAndCount.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2ReadAndCount.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2ReadAndCount.dll"]
