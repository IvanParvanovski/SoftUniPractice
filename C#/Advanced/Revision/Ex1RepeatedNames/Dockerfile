FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex1RepeatedNames/Ex1RepeatedNames.csproj", "Ex1RepeatedNames/"]
RUN dotnet restore "Ex1RepeatedNames/Ex1RepeatedNames.csproj"
COPY . .
WORKDIR "/src/Ex1RepeatedNames"
RUN dotnet build "Ex1RepeatedNames.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex1RepeatedNames.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex1RepeatedNames.dll"]
