FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex2OrderStudents/Ex2OrderStudents.csproj", "Ex2OrderStudents/"]
RUN dotnet restore "Ex2OrderStudents/Ex2OrderStudents.csproj"
COPY . .
WORKDIR "/src/Ex2OrderStudents"
RUN dotnet build "Ex2OrderStudents.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2OrderStudents.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2OrderStudents.dll"]
