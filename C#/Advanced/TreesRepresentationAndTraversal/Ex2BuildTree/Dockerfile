FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex2BuildTree/Ex2BuildTree.csproj", "Ex2BuildTree/"]
RUN dotnet restore "Ex2BuildTree/Ex2BuildTree.csproj"
COPY . .
WORKDIR "/src/Ex2BuildTree"
RUN dotnet build "Ex2BuildTree.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2BuildTree.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2BuildTree.dll"]
