FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["DFS_BFS_Exercise/DFS_BFS_Exercise.csproj", "DFS_BFS_Exercise/"]
RUN dotnet restore "DFS_BFS_Exercise/DFS_BFS_Exercise.csproj"
COPY . .
WORKDIR "/src/DFS_BFS_Exercise"
RUN dotnet build "DFS_BFS_Exercise.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "DFS_BFS_Exercise.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DFS_BFS_Exercise.dll"]
