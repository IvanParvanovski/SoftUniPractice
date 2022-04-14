FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex2TraverseGraphDFS/Ex2TraverseGraphDFS.csproj", "Ex2TraverseGraphDFS/"]
RUN dotnet restore "Ex2TraverseGraphDFS/Ex2TraverseGraphDFS.csproj"
COPY . .
WORKDIR "/src/Ex2TraverseGraphDFS"
RUN dotnet build "Ex2TraverseGraphDFS.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2TraverseGraphDFS.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2TraverseGraphDFS.dll"]
