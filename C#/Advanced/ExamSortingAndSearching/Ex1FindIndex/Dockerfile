FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex1FindIndex/Ex1FindIndex.fsproj", "Ex1FindIndex/"]
RUN dotnet restore "Ex1FindIndex/Ex1FindIndex.fsproj"
COPY . .
WORKDIR "/src/Ex1FindIndex"
RUN dotnet build "Ex1FindIndex.fsproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1FindIndex.fsproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1FindIndex.dll"]
