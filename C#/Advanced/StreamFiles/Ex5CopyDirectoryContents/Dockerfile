FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex5CopyDirectoryContents/Ex5CopyDirectoryContents.csproj", "Ex5CopyDirectoryContents/"]
RUN dotnet restore "Ex5CopyDirectoryContents/Ex5CopyDirectoryContents.csproj"
COPY . .
WORKDIR "/src/Ex5CopyDirectoryContents"
RUN dotnet build "Ex5CopyDirectoryContents.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex5CopyDirectoryContents.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex5CopyDirectoryContents.dll"]
