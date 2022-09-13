FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex2LineNumbers/Ex2LineNumbers.csproj", "Ex2LineNumbers/"]
RUN dotnet restore "Ex2LineNumbers/Ex2LineNumbers.csproj"
COPY . .
WORKDIR "/src/Ex2LineNumbers"
RUN dotnet build "Ex2LineNumbers.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2LineNumbers.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2LineNumbers.dll"]
