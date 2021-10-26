FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex5CompanyRoaster/Ex5CompanyRoaster.csproj", "Ex5CompanyRoaster/"]
RUN dotnet restore "Ex5CompanyRoaster/Ex5CompanyRoaster.csproj"
COPY . .
WORKDIR "/src/Ex5CompanyRoaster"
RUN dotnet build "Ex5CompanyRoaster.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex5CompanyRoaster.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex5CompanyRoaster.dll"]
