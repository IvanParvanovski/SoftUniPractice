FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["ShuffleArray/ShuffleArray.csproj", "ShuffleArray/"]
RUN dotnet restore "ShuffleArray/ShuffleArray.csproj"
COPY . .
WORKDIR "/src/ShuffleArray"
RUN dotnet build "ShuffleArray.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ShuffleArray.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ShuffleArray.dll"]
