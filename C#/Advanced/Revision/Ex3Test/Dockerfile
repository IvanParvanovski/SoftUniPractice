FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex3Test/Ex3Test.csproj", "Ex3Test/"]
RUN dotnet restore "Ex3Test/Ex3Test.csproj"
COPY . .
WORKDIR "/src/Ex3Test"
RUN dotnet build "Ex3Test.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3Test.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3Test.dll"]
