FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["ImplementingStack/ImplementingStack.csproj", "ImplementingStack/"]
RUN dotnet restore "ImplementingStack/ImplementingStack.csproj"
COPY . .
WORKDIR "/src/ImplementingStack"
RUN dotnet build "ImplementingStack.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ImplementingStack.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ImplementingStack.dll"]
