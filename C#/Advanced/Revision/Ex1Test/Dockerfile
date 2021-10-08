FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1Test/Ex1Test.csproj", "Ex1Test/"]
RUN dotnet restore "Ex1Test/Ex1Test.csproj"
COPY . .
WORKDIR "/src/Ex1Test"
RUN dotnet build "Ex1Test.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1Test.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1Test.dll"]
