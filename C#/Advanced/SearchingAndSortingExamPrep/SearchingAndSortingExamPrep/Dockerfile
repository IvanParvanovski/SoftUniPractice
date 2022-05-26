FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["SearchingAndSortingExamPrep/SearchingAndSortingExamPrep.csproj", "SearchingAndSortingExamPrep/"]
RUN dotnet restore "SearchingAndSortingExamPrep/SearchingAndSortingExamPrep.csproj"
COPY . .
WORKDIR "/src/SearchingAndSortingExamPrep"
RUN dotnet build "SearchingAndSortingExamPrep.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SearchingAndSortingExamPrep.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SearchingAndSortingExamPrep.dll"]
