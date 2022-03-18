FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex2Maze/Ex2Maze.csproj", "Ex2Maze/"]
RUN dotnet restore "Ex2Maze/Ex2Maze.csproj"
COPY . .
WORKDIR "/src/Ex2Maze"
RUN dotnet build "Ex2Maze.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2Maze.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2Maze.dll"]
