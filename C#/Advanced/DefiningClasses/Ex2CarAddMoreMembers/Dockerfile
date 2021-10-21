FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex2CarAddMoreMembers/Ex2CarAddMoreMembers.csproj", "Ex2CarAddMoreMembers/"]
RUN dotnet restore "Ex2CarAddMoreMembers/Ex2CarAddMoreMembers.csproj"
COPY . .
WORKDIR "/src/Ex2CarAddMoreMembers"
RUN dotnet build "Ex2CarAddMoreMembers.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2CarAddMoreMembers.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2CarAddMoreMembers.dll"]
