FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex3Classification/Ex3Classification.csproj", "Ex3Classification/"]
RUN dotnet restore "Ex3Classification/Ex3Classification.csproj"
COPY . .
WORKDIR "/src/Ex3Classification"
RUN dotnet build "Ex3Classification.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3Classification.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3Classification.dll"]
