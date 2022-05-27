FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["ExamSortingAndSearching/ExamSortingAndSearching.csproj", "ExamSortingAndSearching/"]
RUN dotnet restore "ExamSortingAndSearching/ExamSortingAndSearching.csproj"
COPY . .
WORKDIR "/src/ExamSortingAndSearching"
RUN dotnet build "ExamSortingAndSearching.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ExamSortingAndSearching.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ExamSortingAndSearching.dll"]
