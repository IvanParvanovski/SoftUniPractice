FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["GraphsLab/GraphsLab.csproj", "GraphsLab/"]
RUN dotnet restore "GraphsLab/GraphsLab.csproj"
COPY . .
WORKDIR "/src/GraphsLab"
RUN dotnet build "GraphsLab.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "GraphsLab.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "GraphsLab.dll"]
