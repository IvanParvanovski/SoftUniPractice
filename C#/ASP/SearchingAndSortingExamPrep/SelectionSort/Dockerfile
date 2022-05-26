FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["SelectionSort/SelectionSort.csproj", "SelectionSort/"]
RUN dotnet restore "SelectionSort/SelectionSort.csproj"
COPY . .
WORKDIR "/src/SelectionSort"
RUN dotnet build "SelectionSort.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SelectionSort.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SelectionSort.dll"]
