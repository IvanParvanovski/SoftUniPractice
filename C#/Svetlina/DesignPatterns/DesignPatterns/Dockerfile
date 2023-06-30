FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["DesignPatterns/DesignPatterns.csproj", "DesignPatterns/"]
RUN dotnet restore "DesignPatterns/DesignPatterns.csproj"
COPY . .
WORKDIR "/src/DesignPatterns"
RUN dotnet build "DesignPatterns.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "DesignPatterns.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DesignPatterns.dll"]
