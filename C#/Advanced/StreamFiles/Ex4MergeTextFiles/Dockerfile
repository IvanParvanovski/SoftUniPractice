FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex4MergeTextFiles/Ex4MergeTextFiles.csproj", "Ex4MergeTextFiles/"]
RUN dotnet restore "Ex4MergeTextFiles/Ex4MergeTextFiles.csproj"
COPY . .
WORKDIR "/src/Ex4MergeTextFiles"
RUN dotnet build "Ex4MergeTextFiles.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex4MergeTextFiles.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex4MergeTextFiles.dll"]
