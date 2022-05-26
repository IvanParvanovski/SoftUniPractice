FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["BubbleSort/BubbleSort.csproj", "BubbleSort/"]
RUN dotnet restore "BubbleSort/BubbleSort.csproj"
COPY . .
WORKDIR "/src/BubbleSort"
RUN dotnet build "BubbleSort.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "BubbleSort.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "BubbleSort.dll"]
