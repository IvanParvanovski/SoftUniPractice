FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex1GraphBFS/Ex1GraphBFS.csproj", "Ex1GraphBFS/"]
RUN dotnet restore "Ex1GraphBFS/Ex1GraphBFS.csproj"
COPY . .
WORKDIR "/src/Ex1GraphBFS"
RUN dotnet build "Ex1GraphBFS.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1GraphBFS.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1GraphBFS.dll"]
