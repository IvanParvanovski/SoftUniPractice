FROM mcr.microsoft.com/dotnet/core/runtime:3.1 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.1 AS build
WORKDIR /src
COPY ["Ex2LineNumbersLab/Ex2LineNumbersLab.csproj", "Ex2LineNumbersLab/"]
RUN dotnet restore "Ex2LineNumbersLab/Ex2LineNumbersLab.csproj"
COPY . .
WORKDIR "/src/Ex2LineNumbersLab"
RUN dotnet build "Ex2LineNumbersLab.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Ex2LineNumbersLab.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Ex2LineNumbersLab.dll"]
