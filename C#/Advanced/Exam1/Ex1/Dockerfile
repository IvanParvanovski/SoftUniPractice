FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1/Ex1.csproj", "Ex1/"]
RUN dotnet restore "Ex1/Ex1.csproj"
COPY . .
WORKDIR "/src/Ex1"
RUN dotnet build "Ex1.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1.dll"]
