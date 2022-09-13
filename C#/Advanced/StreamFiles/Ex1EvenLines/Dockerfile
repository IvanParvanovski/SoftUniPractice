FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex1EvenLines/Ex1EvenLines.csproj", "Ex1EvenLines/"]
RUN dotnet restore "Ex1EvenLines/Ex1EvenLines.csproj"
COPY . .
WORKDIR "/src/Ex1EvenLines"
RUN dotnet build "Ex1EvenLines.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1EvenLines.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1EvenLines.dll"]
