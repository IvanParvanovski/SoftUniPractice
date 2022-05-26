FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["QuickSort/QuickSort.csproj", "QuickSort/"]
RUN dotnet restore "QuickSort/QuickSort.csproj"
COPY . .
WORKDIR "/src/QuickSort"
RUN dotnet build "QuickSort.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "QuickSort.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "QuickSort.dll"]
