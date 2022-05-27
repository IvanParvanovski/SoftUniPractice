FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["SearchingAndSortExam/SearchingAndSortExam.csproj", "SearchingAndSortExam/"]
RUN dotnet restore "SearchingAndSortExam/SearchingAndSortExam.csproj"
COPY . .
WORKDIR "/src/SearchingAndSortExam"
RUN dotnet build "SearchingAndSortExam.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SearchingAndSortExam.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SearchingAndSortExam.dll"]
