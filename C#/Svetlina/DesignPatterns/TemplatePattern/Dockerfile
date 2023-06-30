FROM mcr.microsoft.com/dotnet/runtime:6.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["TemplatePattern/TemplatePattern.csproj", "TemplatePattern/"]
RUN dotnet restore "TemplatePattern/TemplatePattern.csproj"
COPY . .
WORKDIR "/src/TemplatePattern"
RUN dotnet build "TemplatePattern.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "TemplatePattern.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "TemplatePattern.dll"]
