FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["ImplementingLinkedList/ImplementingLinkedList.csproj", "ImplementingLinkedList/"]
RUN dotnet restore "ImplementingLinkedList/ImplementingLinkedList.csproj"
COPY . .
WORKDIR "/src/ImplementingLinkedList"
RUN dotnet build "ImplementingLinkedList.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ImplementingLinkedList.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ImplementingLinkedList.dll"]
