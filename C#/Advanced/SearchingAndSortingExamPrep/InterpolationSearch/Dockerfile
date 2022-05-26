FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["InterpolationSearch/InterpolationSearch.csproj", "InterpolationSearch/"]
RUN dotnet restore "InterpolationSearch/InterpolationSearch.csproj"
COPY . .
WORKDIR "/src/InterpolationSearch"
RUN dotnet build "InterpolationSearch.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "InterpolationSearch.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "InterpolationSearch.dll"]
