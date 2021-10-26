FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex2CreateConstructors/Ex2CreateConstructors.csproj", "Ex2CreateConstructors/"]
RUN dotnet restore "Ex2CreateConstructors/Ex2CreateConstructors.csproj"
COPY . .
WORKDIR "/src/Ex2CreateConstructors"
RUN dotnet build "Ex2CreateConstructors.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2CreateConstructors.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2CreateConstructors.dll"]
