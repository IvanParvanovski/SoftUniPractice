FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex2Test/Ex2Test.csproj", "Ex2Test/"]
RUN dotnet restore "Ex2Test/Ex2Test.csproj"
COPY . .
WORKDIR "/src/Ex2Test"
RUN dotnet build "Ex2Test.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2Test.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2Test.dll"]
