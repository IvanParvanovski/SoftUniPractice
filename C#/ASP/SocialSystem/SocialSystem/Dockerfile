FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["SocialSystem/SocialSystem.csproj", "SocialSystem/"]
RUN dotnet restore "SocialSystem/SocialSystem.csproj"
COPY . .
WORKDIR "/src/SocialSystem"
RUN dotnet build "SocialSystem.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SocialSystem.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SocialSystem.dll"]
