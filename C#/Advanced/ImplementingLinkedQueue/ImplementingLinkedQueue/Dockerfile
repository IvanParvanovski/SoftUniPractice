FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["ImplementingLinkedQueue/ImplementingLinkedQueue.csproj", "ImplementingLinkedQueue/"]
RUN dotnet restore "ImplementingLinkedQueue/ImplementingLinkedQueue.csproj"
COPY . .
WORKDIR "/src/ImplementingLinkedQueue"
RUN dotnet build "ImplementingLinkedQueue.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ImplementingLinkedQueue.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ImplementingLinkedQueue.dll"]
