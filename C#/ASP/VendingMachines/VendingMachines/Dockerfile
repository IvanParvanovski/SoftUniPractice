FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["VendingMachines/VendingMachines.csproj", "VendingMachines/"]
RUN dotnet restore "VendingMachines/VendingMachines.csproj"
COPY . .
WORKDIR "/src/VendingMachines"
RUN dotnet build "VendingMachines.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "VendingMachines.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "VendingMachines.dll"]
