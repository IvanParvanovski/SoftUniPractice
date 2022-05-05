FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex1ConnectedComponents/Ex1ConnectedComponents.csproj", "Ex1ConnectedComponents/"]
RUN dotnet restore "Ex1ConnectedComponents/Ex1ConnectedComponents.csproj"
COPY . .
WORKDIR "/src/Ex1ConnectedComponents"
RUN dotnet build "Ex1ConnectedComponents.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1ConnectedComponents.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1ConnectedComponents.dll"]
