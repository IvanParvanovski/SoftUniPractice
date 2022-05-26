FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex3MatrixPath/Ex3MatrixPath.csproj", "Ex3MatrixPath/"]
RUN dotnet restore "Ex3MatrixPath/Ex3MatrixPath.csproj"
COPY . .
WORKDIR "/src/Ex3MatrixPath"
RUN dotnet build "Ex3MatrixPath.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3MatrixPath.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3MatrixPath.dll"]
