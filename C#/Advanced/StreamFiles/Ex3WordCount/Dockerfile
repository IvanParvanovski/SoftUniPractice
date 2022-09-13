FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex3WordCount/Ex3WordCount.csproj", "Ex3WordCount/"]
RUN dotnet restore "Ex3WordCount/Ex3WordCount.csproj"
COPY . .
WORKDIR "/src/Ex3WordCount"
RUN dotnet build "Ex3WordCount.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3WordCount.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3WordCount.dll"]
