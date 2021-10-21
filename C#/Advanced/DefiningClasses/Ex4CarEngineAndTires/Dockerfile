FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex4CarEngineAndTires/Ex4CarEngineAndTires.csproj", "Ex4CarEngineAndTires/"]
RUN dotnet restore "Ex4CarEngineAndTires/Ex4CarEngineAndTires.csproj"
COPY . .
WORKDIR "/src/Ex4CarEngineAndTires"
RUN dotnet build "Ex4CarEngineAndTires.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex4CarEngineAndTires.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex4CarEngineAndTires.dll"]
