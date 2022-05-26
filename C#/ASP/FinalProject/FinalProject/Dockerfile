FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["FinalProject/FinalProject.csproj", "FinalProject/"]
RUN dotnet restore "FinalProject/FinalProject.csproj"
COPY . .
WORKDIR "/src/FinalProject"
RUN dotnet build "FinalProject.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "FinalProject.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "FinalProject.dll"]
