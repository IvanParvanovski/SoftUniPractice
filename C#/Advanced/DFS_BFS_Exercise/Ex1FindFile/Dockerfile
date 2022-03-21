FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex1FindFile/Ex1FindFile.csproj", "Ex1FindFile/"]
RUN dotnet restore "Ex1FindFile/Ex1FindFile.csproj"
COPY . .
WORKDIR "/src/Ex1FindFile"
RUN dotnet build "Ex1FindFile.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1FindFile.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1FindFile.dll"]
