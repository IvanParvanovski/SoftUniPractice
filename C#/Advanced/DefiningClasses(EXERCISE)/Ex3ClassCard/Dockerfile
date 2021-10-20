FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex3ClassCard/Ex3ClassCard.csproj", "Ex3ClassCard/"]
RUN dotnet restore "Ex3ClassCard/Ex3ClassCard.csproj"
COPY . .
WORKDIR "/src/Ex3ClassCard"
RUN dotnet build "Ex3ClassCard.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3ClassCard.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3ClassCard.dll"]
