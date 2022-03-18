FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex3ShoppingCentre/Ex3ShoppingCentre.csproj", "Ex3ShoppingCentre/"]
RUN dotnet restore "Ex3ShoppingCentre/Ex3ShoppingCentre.csproj"
COPY . .
WORKDIR "/src/Ex3ShoppingCentre"
RUN dotnet build "Ex3ShoppingCentre.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3ShoppingCentre.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3ShoppingCentre.dll"]
