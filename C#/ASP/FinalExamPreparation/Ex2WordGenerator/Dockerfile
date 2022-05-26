FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex2WordGenerator/Ex2WordGenerator.csproj", "Ex2WordGenerator/"]
RUN dotnet restore "Ex2WordGenerator/Ex2WordGenerator.csproj"
COPY . .
WORKDIR "/src/Ex2WordGenerator"
RUN dotnet build "Ex2WordGenerator.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2WordGenerator.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2WordGenerator.dll"]
