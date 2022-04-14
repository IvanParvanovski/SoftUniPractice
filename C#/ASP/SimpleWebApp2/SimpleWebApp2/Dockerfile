FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["SimpleWebApp2/SimpleWebApp2.csproj", "SimpleWebApp2/"]
RUN dotnet restore "SimpleWebApp2/SimpleWebApp2.csproj"
COPY . .
WORKDIR "/src/SimpleWebApp2"
RUN dotnet build "SimpleWebApp2.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SimpleWebApp2.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SimpleWebApp2.dll"]
