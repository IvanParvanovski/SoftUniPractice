FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex4RandomizeCards/Ex4RandomizeCards.csproj", "Ex4RandomizeCards/"]
RUN dotnet restore "Ex4RandomizeCards/Ex4RandomizeCards.csproj"
COPY . .
WORKDIR "/src/Ex4RandomizeCards"
RUN dotnet build "Ex4RandomizeCards.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex4RandomizeCards.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex4RandomizeCards.dll"]
