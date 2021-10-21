FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex3CarConstructors/Ex3CarConstructors.csproj", "Ex3CarConstructors/"]
RUN dotnet restore "Ex3CarConstructors/Ex3CarConstructors.csproj"
COPY . .
WORKDIR "/src/Ex3CarConstructors"
RUN dotnet build "Ex3CarConstructors.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3CarConstructors.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3CarConstructors.dll"]
