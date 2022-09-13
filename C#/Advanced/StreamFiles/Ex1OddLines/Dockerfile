FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex1OddLines/Ex1OddLines.csproj", "Ex1OddLines/"]
RUN dotnet restore "Ex1OddLines/Ex1OddLines.csproj"
COPY . .
WORKDIR "/src/Ex1OddLines"
RUN dotnet build "Ex1OddLines.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1OddLines.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1OddLines.dll"]
