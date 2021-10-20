FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex2CalculationWithFractions/Ex2CalculationWithFractions.csproj", "Ex2CalculationWithFractions/"]
RUN dotnet restore "Ex2CalculationWithFractions/Ex2CalculationWithFractions.csproj"
COPY . .
WORKDIR "/src/Ex2CalculationWithFractions"
RUN dotnet build "Ex2CalculationWithFractions.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2CalculationWithFractions.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2CalculationWithFractions.dll"]
