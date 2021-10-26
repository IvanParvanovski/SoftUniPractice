FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex5CompanyRoster/Ex5CompanyRoster.csproj", "Ex5CompanyRoster/"]
RUN dotnet restore "Ex5CompanyRoster/Ex5CompanyRoster.csproj"
COPY . .
WORKDIR "/src/Ex5CompanyRoster"
RUN dotnet build "Ex5CompanyRoster.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex5CompanyRoster.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex5CompanyRoster.dll"]
