FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex3CheckStudents/Ex3CheckStudents.csproj", "Ex3CheckStudents/"]
RUN dotnet restore "Ex3CheckStudents/Ex3CheckStudents.csproj"
COPY . .
WORKDIR "/src/Ex3CheckStudents"
RUN dotnet build "Ex3CheckStudents.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3CheckStudents.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3CheckStudents.dll"]
