FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex2SpecialVariations/Ex2SpecialVariations.csproj", "Ex2SpecialVariations/"]
RUN dotnet restore "Ex2SpecialVariations/Ex2SpecialVariations.csproj"
COPY . .
WORKDIR "/src/Ex2SpecialVariations"
RUN dotnet build "Ex2SpecialVariations.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2SpecialVariations.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2SpecialVariations.dll"]
