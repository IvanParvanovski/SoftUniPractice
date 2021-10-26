FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex6SpeedRacing/Ex6SpeedRacing.csproj", "Ex6SpeedRacing/"]
RUN dotnet restore "Ex6SpeedRacing/Ex6SpeedRacing.csproj"
COPY . .
WORKDIR "/src/Ex6SpeedRacing"
RUN dotnet build "Ex6SpeedRacing.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex6SpeedRacing.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex6SpeedRacing.dll"]
