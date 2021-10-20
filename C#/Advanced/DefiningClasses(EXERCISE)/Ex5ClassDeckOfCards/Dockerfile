FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex5ClassDeckofCards/Ex5ClassDeckofCards.csproj", "Ex5ClassDeckofCards/"]
RUN dotnet restore "Ex5ClassDeckofCards/Ex5ClassDeckofCards.csproj"
COPY . .
WORKDIR "/src/Ex5ClassDeckofCards"
RUN dotnet build "Ex5ClassDeckofCards.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex5ClassDeckofCards.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex5ClassDeckofCards.dll"]
