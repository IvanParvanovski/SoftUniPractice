FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["MyFirstWeb/MyFirstWeb.csproj", "MyFirstWeb/"]
RUN dotnet restore "MyFirstWeb/MyFirstWeb.csproj"
COPY . .
WORKDIR "/src/MyFirstWeb"
RUN dotnet build "MyFirstWeb.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "MyFirstWeb.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "MyFirstWeb.dll"]
