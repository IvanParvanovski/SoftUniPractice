FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex1NumbersSorter/Ex1NumbersSorter.csproj", "Ex1NumbersSorter/"]
RUN dotnet restore "Ex1NumbersSorter/Ex1NumbersSorter.csproj"
COPY . .
WORKDIR "/src/Ex1NumbersSorter"
RUN dotnet build "Ex1NumbersSorter.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1NumbersSorter.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1NumbersSorter.dll"]
