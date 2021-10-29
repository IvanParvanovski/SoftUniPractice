FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex2/Ex2.csproj", "Ex2/"]
RUN dotnet restore "Ex2/Ex2.csproj"
COPY . .
WORKDIR "/src/Ex2"
RUN dotnet build "Ex2.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2.dll"]
