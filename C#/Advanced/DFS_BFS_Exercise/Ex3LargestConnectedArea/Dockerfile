FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex3LargestConnectedArea/Ex3LargestConnectedArea.csproj", "Ex3LargestConnectedArea/"]
RUN dotnet restore "Ex3LargestConnectedArea/Ex3LargestConnectedArea.csproj"
COPY . .
WORKDIR "/src/Ex3LargestConnectedArea"
RUN dotnet build "Ex3LargestConnectedArea.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3LargestConnectedArea.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3LargestConnectedArea.dll"]
