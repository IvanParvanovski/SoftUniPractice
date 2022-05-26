FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["InsertionSort/InsertionSort.csproj", "InsertionSort/"]
RUN dotnet restore "InsertionSort/InsertionSort.csproj"
COPY . .
WORKDIR "/src/InsertionSort"
RUN dotnet build "InsertionSort.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "InsertionSort.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "InsertionSort.dll"]
