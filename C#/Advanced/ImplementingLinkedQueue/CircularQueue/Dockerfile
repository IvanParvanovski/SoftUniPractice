FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["CircularQueue/CircularQueue.csproj", "CircularQueue/"]
RUN dotnet restore "CircularQueue/CircularQueue.csproj"
COPY . .
WORKDIR "/src/CircularQueue"
RUN dotnet build "CircularQueue.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "CircularQueue.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "CircularQueue.dll"]
