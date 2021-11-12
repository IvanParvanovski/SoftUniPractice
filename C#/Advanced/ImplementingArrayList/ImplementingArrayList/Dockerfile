FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["ImplementingArrayList/ImplementingArrayList.csproj", "ImplementingArrayList/"]
RUN dotnet restore "ImplementingArrayList/ImplementingArrayList.csproj"
COPY . .
WORKDIR "/src/ImplementingArrayList"
RUN dotnet build "ImplementingArrayList.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ImplementingArrayList.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ImplementingArrayList.dll"]
