FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["LinearSeatch/LinearSeatch.csproj", "LinearSeatch/"]
RUN dotnet restore "LinearSeatch/LinearSeatch.csproj"
COPY . .
WORKDIR "/src/LinearSeatch"
RUN dotnet build "LinearSeatch.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "LinearSeatch.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "LinearSeatch.dll"]
