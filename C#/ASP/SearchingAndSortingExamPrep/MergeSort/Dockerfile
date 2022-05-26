FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["MergeSort/MergeSort.csproj", "MergeSort/"]
RUN dotnet restore "MergeSort/MergeSort.csproj"
COPY . .
WORKDIR "/src/MergeSort"
RUN dotnet build "MergeSort.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MergeSort.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MergeSort.dll"]
