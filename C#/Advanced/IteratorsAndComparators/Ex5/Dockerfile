FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex5/Ex5.csproj", "Ex5/"]
RUN dotnet restore "Ex5/Ex5.csproj"
COPY . .
WORKDIR "/src/Ex5"
RUN dotnet build "Ex5.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex5.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex5.dll"]
