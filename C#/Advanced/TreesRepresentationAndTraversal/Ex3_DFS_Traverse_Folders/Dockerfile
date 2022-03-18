FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex3_DFS_Traverse_Folders/Ex3_DFS_Traverse_Folders.csproj", "Ex3_DFS_Traverse_Folders/"]
RUN dotnet restore "Ex3_DFS_Traverse_Folders/Ex3_DFS_Traverse_Folders.csproj"
COPY . .
WORKDIR "/src/Ex3_DFS_Traverse_Folders"
RUN dotnet build "Ex3_DFS_Traverse_Folders.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3_DFS_Traverse_Folders.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3_DFS_Traverse_Folders.dll"]
