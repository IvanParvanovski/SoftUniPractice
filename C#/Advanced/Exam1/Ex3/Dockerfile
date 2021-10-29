FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Еx3/Еx3.csproj", "Еx3/"]
RUN dotnet restore "Еx3/Еx3.csproj"
COPY . .
WORKDIR "/src/Еx3"
RUN dotnet build "Еx3.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Еx3.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Еx3.dll"]
