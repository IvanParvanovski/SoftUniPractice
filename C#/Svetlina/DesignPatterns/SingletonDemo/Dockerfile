FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["SingletonDemo/SingletonDemo.csproj", "SingletonDemo/"]
RUN dotnet restore "SingletonDemo/SingletonDemo.csproj"
COPY . .
WORKDIR "/src/SingletonDemo"
RUN dotnet build "SingletonDemo.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SingletonDemo.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SingletonDemo.dll"]
