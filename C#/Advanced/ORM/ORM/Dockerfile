FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["ORM/ORM.csproj", "ORM/"]
RUN dotnet restore "ORM/ORM.csproj"
COPY . .
WORKDIR "/src/ORM"
RUN dotnet build "ORM.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ORM.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ORM.dll"]
