FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["BinarySearch/BinarySearch.csproj", "BinarySearch/"]
RUN dotnet restore "BinarySearch/BinarySearch.csproj"
COPY . .
WORKDIR "/src/BinarySearch"
RUN dotnet build "BinarySearch.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "BinarySearch.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "BinarySearch.dll"]
