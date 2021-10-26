FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["Ex3OldestFamilyMember/Ex3OldestFamilyMember.csproj", "Ex3OldestFamilyMember/"]
RUN dotnet restore "Ex3OldestFamilyMember/Ex3OldestFamilyMember.csproj"
COPY . .
WORKDIR "/src/Ex3OldestFamilyMember"
RUN dotnet build "Ex3OldestFamilyMember.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex3OldestFamilyMember.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex3OldestFamilyMember.dll"]
