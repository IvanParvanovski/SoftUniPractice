FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex3CopyBinaryFiles/Ex3CopyBinaryFiles.csproj", "Ex3CopyBinaryFiles/"]
RUN dotnet restore "Ex3CopyBinaryFiles/Ex3CopyBinaryFiles.csproj"
COPY . .
WORKDIR "/src/Ex3CopyBinaryFiles"
RUN dotnet build "Ex3CopyBinaryFiles.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3CopyBinaryFiles.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3CopyBinaryFiles.dll"]
